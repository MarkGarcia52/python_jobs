# Invite anyone to dinner
# Make a list of people you want to invite to dinner
# Print a message to each person inviting them to dinner

dinner_invitation = ['Gabe', 'Mom', 'Grandpa', 'Grandma', 'Christian', 'Uncle Mark']
print(f"Hey {dinner_invitation[0]}! I'm inviting you to dinner!")
print(f"Hey {dinner_invitation[1]}! I'm inviting you to dinner!")
print(f"Hey {dinner_invitation[2]}! I'm inviting you to dinner!")
print(f"Hey {dinner_invitation[3]}! I'm inviting you to dinner!")
print(f"Hey {dinner_invitation[4]}! I'm inviting you to dinner!")
print(f"Hey {dinner_invitation[5]}! I'm inviting you to dinner!")

# You heard that someone cannot attend the dinner
# You need to send out new invitations
# Think of someone else to invite
# Add a print call starting with the name of guest who can't make it
# Modify list, replacing the name of the guest who can't make it,
# With the name of the new person you are inviting

print(f"Unfortunately, {dinner_invitation[0]} can't make it to dinner tonight.")
dinner_invitation = ['Gabe', 'Mom', 'Grandpa', 'Grandma', 'Christian', 'Uncle Mark']
del dinner_invitation[0]
dinner_invitation.insert(0, 'Tasha')
print(f"Hey {dinner_invitation[0]}! I'm inviting you to dinner!")
print(f"Hey {dinner_invitation[1]}! I'm inviting you to dinner!")
print(f"Hey {dinner_invitation[2]}! I'm inviting you to dinner!")
print(f"Hey {dinner_invitation[3]}! I'm inviting you to dinner!")
print(f"Hey {dinner_invitation[4]}! I'm inviting you to dinner!")
print(f"Hey {dinner_invitation[5]}! I'm inviting you to dinner!")

# You found a bigger dinner table, so now more space is available
# Think of three more to invite

print(f"Hey so they gave us a bigger table than expected, so I plan on inviting more people!")
dinner_invitation.insert(0,'Talene')
dinner_invitation.insert(3,'David')
dinner_invitation.append('Izyck')
print(f"I've invited you, {dinner_invitation[0]}, to dinner because we got a bigger table than expected!")
print(f"I've invited you, {dinner_invitation[1]}, to dinner because we got a bigger table than expected!")
print(f"I've invited you, {dinner_invitation[2]}, to dinner because we got a bigger table than expected!")
print(f"I've invited you, {dinner_invitation[3]}, to dinner because we got a bigger table than expected!")
print(f"I've invited you, {dinner_invitation[4]}, to dinner because we got a bigger table than expected!")
print(f"I've invited you, {dinner_invitation[5]}, to dinner because we got a bigger table than expected!")
print(f"I've invited you, {dinner_invitation[6]}, to dinner because we got a bigger table than expected!")
print(f"I've invited you, {dinner_invitation[7]}, to dinner because we got a bigger table than expected!")

# You can no longer invite 6 of your 8 total guests.
# Send them a personalized message and pop() them from list.

print(f"So I guess I can only invite two guests. I plan on inviting less people than before.")
no_invite = dinner_invitation.pop()
message = (f"I'm sorry {no_invite}, but you are no longer invited.")
print(message)
print(f"So I guess I can only invite two guests. I plan on inviting less people than before.")
no_invite = dinner_invitation.pop()
message = (f"I'm sorry {no_invite}, but you are no longer invited.")
print(message)
print(f"So I guess I can only invite two guests. I plan on inviting less people than before.")
no_invite = dinner_invitation.pop()
message = (f"I'm sorry {no_invite}, but you are no longer invited.")
print(message)
print(f"So I guess I can only invite two guests. I plan on inviting less people than before.")
no_invite = dinner_invitation.pop()
message = (f"I'm sorry {no_invite}, but you are no longer invited.")
print(message)
print(f"So I guess I can only invite two guests. I plan on inviting less people than before.")
no_invite = dinner_invitation.pop()
message = (f"I'm sorry {no_invite}, but you are no longer invited.")
print(message)
print(f"So I guess I can only invite two guests. I plan on inviting less people than before.")
no_invite = dinner_invitation.pop()
message = (f"I'm sorry {no_invite}, but you are no longer invited.")
print(message)
print(f"So I guess I can only invite two guests. I plan on inviting less people than before.")
no_invite = dinner_invitation.pop()
message = (f"I'm sorry {no_invite}, but you are no longer invited.")
print(message)

# Send an invite to the last people on your list.

still_invited = dinner_invitation
still_invited = (f"Hey {dinner_invitation[0]}, you are still invited to dinner!")
print(still_invited)
still_invited = dinner_invitation
still_invited = (f"Hey {dinner_invitation[1]}, you are still invited to dinner!")
print(still_invited)

# Remove the last two people using the del method.

print(dinner_invitation)
del dinner_invitation[0]
del dinner_invitation[1]
print(dinner_invitation)










