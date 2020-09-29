from split_settings.tools import optional, include

include(
    'base/*.py',

    optional('local/*.py'),  # we can load any other settings from local folder
)