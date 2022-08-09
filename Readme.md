# MaintenanceKeep

MaintenanceKeep is a program that will help you keep track of tasks that need to be done repeatedly. It includes a
dashboard, and a series of URLs that you can access to notify the system that tasks have been completed. It's
recommended to create QR codes for these URLs, so that you can easily check off tasks from everywhere.

Some examples of things that you can keep track of

- When to change the oil in your car
- When your HVAC filter needs to be replaced
- When you need to renew your license

## Why not keep this on a "to do" list?

Some tasks always need doing - it's just a matter of time before they come due again. It's nice to have a self-hosted
system to manage these tasks for you, so you know the state of your maintenance work at a glance

## Limitations

This is a quick and dirty server which is intended to have less than 100 tasks, and be shared within one household. It
would need to be refactored to be used for other use cases.

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

- Timestamps are cheap - make this be append only. Then we can just grab the max timestamp per name.