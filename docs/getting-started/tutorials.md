# Tutorials

After following [the steps to install and launch the application](installation.md), you can now start using it.
Begin by opening [http://localhost:3000](http://localhost:3000) in a browser.

## Login

Currently there are multiple demo accounts that come with the installation.
`Admin` and `Gardener-1` through `Gardener-4`. All of them have the password `1234`.
Each one has different permissions for different Companies and Gardens.

For an exploration of the app, it's recommended to choose the Admin account.
Simply enter the username (`Admin`) in the `Email` field and the password (`1234`) in the password field and press `login`.

## Sign up

Alternatively, you can create a new account by clicking on `Sign up for free` underneath the login fields.
Simply follow the steps on screen until you reach the `Verification` step.
Since verification isn't implemented yet, just press confirm without entering anything.

Next you will be prompted to create a company and a garden.
Follow the steps on screen and you will end up on the same dashboard as you would have with logging in.

## The main application

There are three main tabs: [`Dashboard`](#dashboard), [`Crops`](#crops) and [`3D`](#3d). Every tab is comprised of widgets.
Every widget can be toggled with the `widgets` button in the top right corner.
If you see an empty page, make sure some widgets are turned on.

### Changing current company and garden

In the application, first click on the profile picture in the top right corner followed by `Administration`.
Select the company and garden you want and click on `save`.

### Dashboard

The dashboard contains a widget showing the current and forecasted weather and a map showing the current garden.

### Crops

The crops tab consists of a table showing the beds of the current garden.
Clicking on one of the gardens shows the crops of the clicked bed in the table instead.

### 3D

TODO

### Settings

Once you are logged in, click on the profile picture in the top right corner, and then on `Settings`.

#### Change user info

On the left side you can change user info like username and password.
Just change the displayed values and click save.

#### Manage company and garden, including permissions

The menu on the left side allows you to add or remove permissions for other users to access the current company or garden.
Additionally, if you have the required permissions, you can delete the current company and garden.
Lastly, at the top of the right side is a button to add or modify a picture of the garden that will be displayed on the map.

### Logout

To log out the current user, simply click on the profile picture and select `Logout`.
