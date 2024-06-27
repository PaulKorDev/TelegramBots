# About what?
These are my old telegram bots on Python, which I wrote when I still studied at school.

## Anonymous communication
The bot is a mini social network. This bot connects 2 people and allows them to communicate, holding their real personalities a secret. The bot sends messages to the recipient on his own behalf. This is not a random chat, you find the user by nickname.

First, the user must create a pseudonym, and then he can find the interlocutor

Bot has two modes: simple conversation and super private
I wrote this bot a long ago, so I dont remember what functionality is now implemented in it.

Simple conversation mode

Menu:
- Account settings,
- My dialogs
- Search for the interlocutor
- Change the nickname.
Chat menu: block the user.

Super private mode:

All messages are automatically deleted, after reading them by the recipient.

User oportunities:
1. /(start, menu) - the bot checks ID of user in the database and his nickname, and displays the menu. If the user is not in the database, then the user is thrown into registration.
2. Function. Registration: The user is invited to come up with a nickname that is entered in the database and will be used to contact other users. Nick can be changed in the future.
3. Menu:
- Change the nickname
- Find the user
- Fast contacts - added users (Like frends in social networks)
- About the bot - description of the bot + nickname of the creator of the bot (my)
- List of commands
- Account settings: notifications (ON/Off), delete account, hide yourself from the search,
- Undread messages (with an icon of quantity)
- Black list of users

4. /Help - commands and their description that users can use in the process of communication
5. During communication - /Add "Nick" - another user may agree or not with the fact that he will be on the list of friends of his interlocutor
6. Section - Messages: "You received a message from" + Inline buttons with nicknames, when you press on, a chat opens.
7. In the chat:
- The sender: change, remove,
- At the recipient: read, answer
7.1.1. change:
7.1.2. delete:
7.2.1. Read: the message is deleted, and the sender receives a message about reading + the message itself with partially deleted letters
7.2.2. Reply: a person cannot write to you until you answer (5 minutes are given to the answer, then the message is simply marked with read) + the sender's message changes to "(nickname) the answer"
8. In the description of the bot, add according to what principle communication takes place: communication goes on one message ...; There is no correspondence story, all messages live until they read them
? Commands and their description (can add buttons):
- /Blacklist - Add the user to blacklist

## Humorous personal growth course
This bot  is a comic parody of personal growth courses

Bot who preaches humorous teaching
Elements:
- Slider
- Test slider with Inline
- Photos with a choice of answer
- Entering the text to a certain result
- Processing of excess text
- tracking at what moment the user and his actions
- user's entry into the database and his answers
- sending photos individually processed
