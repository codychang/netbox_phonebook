from setuptools import find_packages, setup

setup(
    name='netbox_phonebook',
    version='0.1',
    description='Netbox Phonebook - User phone number management plugin for NetBox.',
    author='Cody Chang',
    author_email='codychangus@icloud.com',
    url='https://github.com/codychang/netbox_phonebook',
    license='MIT',
    install_requires=[
        'phonenumbers',
        'django-phonenumber-field',
        'django-import-export',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
