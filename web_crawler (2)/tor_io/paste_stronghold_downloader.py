import stem.control

import objects.paste
import objects.paste_collection


class PasteStrongholdDownloader(object):
    def download_pastes(self):
        PasteStrongholdDownloader.renew_connection()

        return objects.paste_collection.PasteCollection.from_pastes_url()

    @staticmethod
    def renew_connection():
        with stem.control.Controller.from_port(port=9051) as controller:
            controller.authenticate(password='my_password')
            controller.signal(stem.Signal.NEWNYM)
