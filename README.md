# **Octodragon - Remastered**
## IoT Qualcomm Dragonboard 410c Project

### Inspiration
We have a bunch buttons lying around our keyboard, so we made a tool to use them.

### What it does
The Octodragon connects a bunch of hotkeys to the keys. It then sends the events over the internet to a computer where they are processed

### How we built it
We started by connecting hotkeys to keys. We then built a GUI to listen for events and transmit events from the input to the computer. We used the UI for users to easily choose what actions each event triggers.

### Challenges we ran into
We spent the majority of our time setting up the GUI and how to interface the interface with the keys.

It was also difficult to figure out which hotkeys to use for each key. For example, some hotkeys required a module and others didn't.

We had to filter each key differently. For the letter "a", we needed a filter so it doesn't register held down keys quickly.

### Accomplishments that we're proud of
We wrote code separately and it worked when we connected everything together. We also utilized many different disciplines like hardware, IOT, and user interfaces.

### What we learned
how to communicate between the hotkeys and keys
how to filter the held down keys
how to start a exe for general use
how to make a user interface in python
how to somewhat multithreading in python

### What's next for Octodragon
Allow a way to easily add or delete keys and hotkeys
Make the input and output scalable
This is a remastered version, but it still requires some work before it's completely usable


### Built With
python
tkinter

As a user, I can use sensors to transmit signals into events on the computer

Gallery Here: https://devpost.com/software/octodragon


******************************************************************************************************************************

### __Contributors__

    Christopher Lin
      
    Garey Fleeman
    
    Steven Landis
    
    Kiet Nyugen
 
