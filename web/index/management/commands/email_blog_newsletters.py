import random
from django.core.mail import get_connection, EmailMultiAlternatives
from django.core.management import BaseCommand
from django.template.loader import render_to_string
from index.models import BlogEntry, Subscriber
from index.views import render_blog_peek


class Command(BaseCommand):
    help = "Blog emails from newsletters@nnjoshi.co"

    open_text_options = [
        "Fresh and New!", "Read Now!", "Newly Out!", "nnjoshi.co Presents!",
        "Out Now!", "Interesting Read!"
    ]

    def handle(self, *args, **options):
        connection = get_connection()  # uses SMTP server specified in settings

        # If you don't open the connection manually,
        # Django will automatically open, then tear down
        # the connection in msg.send()
        connection.open()

        blog_entry = BlogEntry.objects.filter(is_published=True).latest(
            'created')

        html_content = render_to_string('newsletter.html.j', {
            "render_blog_peek": render_blog_peek,
            "blog_entry": blog_entry,
            "is_ns": True
        })

        email_list = [subs.email for subs in Subscriber.objects.all()]

        text_content = "This message requires HTML email support" \
                       "\nNo worries!" \
                       "\nRead the article here " \
                       "http://nnjoshi.co/blog/post/%s" % blog_entry.slug
        for email in email_list:
            msg = EmailMultiAlternatives(
                "%s %s" % (
                    random.choice(self.open_text_options), blog_entry.title),
                text_content, "Newsletters@nnjoshi.co <newsletters@nnjoshi.co>",
                [email], connection=connection)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            print "sending to %s" % email

        connection.close()
