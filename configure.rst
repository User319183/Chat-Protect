
Configuring the bot
========
Chat Protect has so much to make it flexible. Let's go through the configure commands!

Bypassing
========
There are three options you have for bypassing. One is bypassing a user, this allows (a) specified user(s) to be bypassed from being censored by Chat Protect.
Two is bypassing a role, this allows a user, or users, to be bypassed in certin roles. This is better if you want a team of staff to not be censored when
messaging in chat. Three is bypassing a channel. This can be useful if you want members to be able to say anything they want in whatever channel is bypassed.
This is good for debates, arguments, or whatever your usecase may be. You are also able to view the ID's of who & what is bypassed by doing `/view_bypass`


.. image:: https://github.com/User319183/Chat-Protect/blob/main/assets/bypass.png
  :width: 400


Adding, removing, viewing censored words, & clearing the word list
========
Adding your own words to Chat Protect is easy yet may cause some confusion. You can add text to the censor list by doing `/add whattocensor`.
The bot uses an advanced filter to remove symbols, spaces, and latin characters (i.e., "à" , "ć") which means when adding a word/phrase/link 
to the bot, you can not include any symbols, spaces, and latin characters due to how sensitive it is right now. This means if you were to add 
a phrase it would need to look like `/add thisisatest` (this is a test) and for a link, it would look like `/add httpsthisisatestcom` (https://thisisatest.com). 
For removing words from the censor list, you would do `/remove whattouncensor`. Viewing the censor list allows you to just view all the banned words the bot will
filter, this requires no options during command usage. Clearing the censor list means to erase all of the contents of the banned words. Everything that has been
cleared. Each word can still be added back.

.. image:: https://github.com/User319183/Chat-Protect/blob/main/assets/add.png
  :width: 400

.. image:: https://github.com/User319183/Chat-Protect/blob/main/assets/remove.png
  :width: 400

.. image:: https://github.com/User319183/Chat-Protect/blob/main/assets/list.png
  :width: 400

.. image:: https://github.com/User319183/Chat-Protect/blob/main/assets/clear_list.png
  :width: 400


Embeds
========
When doing `/embeds` you will get an option called `set`. Then after pressing the command you will get `enabled` and `disabled`. If you want the censor message
to show when a member says a blacklisted word this will show them the message. If you don't, you can set this to `disabled`. By default, the censor message will 
show. No matter the setting, +1 will be added to the user's amount of strikes.

.. image:: https://github.com/User319183/Chat-Protect/blob/main/assets/embeds.png
  :width: 400


Logchannel
========
By default, there will be no log channel set. You can change this by doing `/logchannel` and typing a Discord text channel. This will allow the bot to log when a
blacklisted word gets sent to that channel. **Something to keep note of:** The `object ID` is a key that gives us information in the database. We use this information
to debug the bot in guilds. 

.. image:: https://github.com/User319183/Chat-Protect/blob/main/assets/logchannel.png
  :width: 400


Preset
========
The `/preset` command is a command that does the words for you. The command gives you a option called `filter` and inside of that there is `racisim`, `bad word`, and 
`toxicity`. This automaticly clears your previous censor list and adds these new pre-built lists.

.. image:: https://github.com/User319183/Chat-Protect/blob/main/assets/preset.png
  :width: 400


Strikes
========
Currently, you can view & add strikes to users. Viewing strikes means you can view how many warns a moderator/the bot has given them. Updating strikes means you can
add or remove any amount of strikes to a user. 

.. image:: https://github.com/User319183/Chat-Protect/blob/main/assets/update_strikes.png
  :width: 40
  
.. image:: https://github.com/User319183/Chat-Protect/blob/main/assets/view_strikes.png
  :width: 400

Table of Contents
========
Missed any part of the documentation you want to read? `Click this text to be redirected to the Table of Contents  <https://github.com/User319183/Chat-Protect/blob/main/table_of_contents.rst>`_
