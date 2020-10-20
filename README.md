Vue.js

    npm install copy-webpack-plugin pug axios vue-axios vue-router vue-codemirror
    vue-sse vuex --save-dev

    npm run dev

Celery

    celery -A code_training worker -l INFO

Generate message files for a desired language
    python manage.py makemessages -l ru
 
After adding translations to the .po files, compile the messages

    python manage.py compilemessages
