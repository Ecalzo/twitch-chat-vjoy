## Architecture
* 1 Queue
* 1 producer
* 1 consumer

- Producer will read and parse chat for commands then push to the Queue
- Consumer will read the latest entry in the queue and execute it in game