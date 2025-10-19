# task-setter
set tasks for safia to do

[![Athena Award Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Faward.athena.hackclub.com%2Fapi%2Fbadge)](https://award.athena.hackclub.com?utm_source=readme)

this is my second api project. it is a monorepo so i made the backend and frontend in this repo. 

what i tried to do better with this project was adding more fields to the api form, plus i really like my anonymous feature where even if you type in your name but tick the anonymous box then it will make your submission anonymous. i also used sqlite this time instead of a temporary database so that the api data saves even if the server is restarted. another thing i did that i'd been wanting to do for the last project was to be able to delete items.

i did try to add authentication using jwt tokens, but i realised it was more complicated than i thought so it might have been easier to start over to integrate that feature. i also tried to call a date api to change the days left to do a task, but that got complicated when i switched to sqlite.

anyways, here are the links:

frontend: https://safias-task-setter.onrender.com

backend: https://task-setter.onrender.com
