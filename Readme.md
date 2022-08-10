# MaintenanceKeep

MaintenanceKeep is a program that will help you keep track of tasks that need to be done repeatedly. It includes a
dashboard, and a series of URLs that you can access to notify the system that tasks have been completed. It's
recommended to create QR codes for these URLs, so that you can easily check off tasks from everywhere.

<img width="724" alt="Screen Shot 2022-08-10 at 12 05 39 AM" src="https://user-images.githubusercontent.com/10187351/183820075-21d150e5-bd0a-45af-936a-07d6a0b2dcb1.png">


Some examples of things that you can keep track of

- When to change the oil in your car
- When your HVAC filter needs to be replaced
- When you need to renew your license

## Why not keep this on a "to do" list?

Some tasks always need doing - it's just a matter of time before they come due again. It's nice to have a self-hosted
system to manage these tasks for you, so you know the state of your maintenance work at a glance

## Limitations

This is a quick and dirty server which was intended to have less than 100 tasks, and be shared within one household. It may not scale very well if you have too many concurrent connections, or too many tasks to complete.

## API


#### `@app.route('/hello')`

Prints hello

#### `@app.route('/status/raw')`

Prints out the contents of the current backing file

#### `@app.route('/status')`
#### `@app.route('/')`

Prints out the status page that lists all tasks

#### `@app.route('/update/<name>')`

Adds a task update to the database, and prints whether the call succeeded

#### `@app.route('/add/<name>/<duration>')`

Adds a brand new task to the database, and prints whether it succeeded

#### `@app.route('/help')`

A testing page that lets you add and update tasks

## How to read the status page

Each row is a task that needs to be completed every so often. The tasks on the board are color coded based on how much time you have left to complete it

- green
  - you have more than 50% of the time left
- yellowgreen
  - you have more than 20% of the time left
- yellow
  - you still have time, but less than 20% left
- red
  - you are overdue

## How to read the data file

This is an example `data.txt` file

```csv
do the dishes,10,1660021049
wash the dog,2419200,1660021119
```

The columns are

|Task title|How often it should be done (sec)|The last time it was done, in epoch numbers.|
|-|-|-|
|wash the dog|2419200|1660021119|

## Roadmap

- Will create a page that shows previous access times for each of the tasks
- Would be obviously be better if this was a sqlite db
- Remove index file generation - no need to write it to disk if we will generate it anew every time