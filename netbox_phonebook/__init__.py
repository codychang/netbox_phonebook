from extras.plugins import PluginConfig

class PhonebookConfig(PluginConfig):
    name = 'netbox_phonebook'
    verbose_name = 'netbox_phonebook'
    description = 'Netbox Phonebook - User phone number management plugin for NetBox.'
    version = '0.1'
    author = 'Cody Chang'
    author_email = 'codychangus@icloud.com'
    base_url = 'netbox_phonebook'
    required_settings = []
    default_settings = {}
    caching_config = {}
    django_apps=['import_export']

config = PhonebookConfig