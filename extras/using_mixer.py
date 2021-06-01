from mixer.backend.django import mixer


# Generate model's instance and save to db
tree = mixer.blend('imibio_tree_ecological_data.TreeEcologicalData')

print message.content  # Some like --> necessitatibus voluptates animi molestiae dolores...

print message.client.username  # Some like --> daddy102

print message.client.name  # Some like --> Clark Llandrindod

# Generate a few pieces
messages = mixer.cycle(4).blend('someapp.message')
