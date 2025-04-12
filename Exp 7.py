import random

p = int(input('Enter a prime number: '))
g = int(input('Enter a number: '))

class Participant:
    def __init__(self):
        self.private_key = random.randint(1, p)

    def publish(self):
        return pow(g, self.private_key, p)

    def compute_secret(self, received_key):
        return pow(received_key, self.private_key, p)

class Eavesdropper:
    def __init__(self):
        self.a, self.b = random.randint(1, p), random.randint(1, p)

    def publish(self, i):
        return pow(g, [self.a, self.b][i], p)

    def compute_secret(self, received_key, i):
        return pow(received_key, [self.a, self.b][i], p)

alice, bob, eve = Participant(), Participant(), Eavesdropper()

print(f'Alice private key: {alice.private_key}')
print(f'Bob private key: {bob.private_key}')
print(f'Eve private keys: {eve.a}, {eve.b}')

ga, gb = alice.publish(), bob.publish()
gea, geb = eve.publish(0), eve.publish(1)

print(f'Alice public key: {ga}')
print(f'Bob public key: {gb}')
print(f'Eve public keys: {gea}, {geb}')

sa, sb = alice.compute_secret(gea), bob.compute_secret(geb)
sea, seb = eve.compute_secret(ga, 0), eve.compute_secret(gb, 1)

print(f'Alice computed key: {sa}')
print(f'Eve computed key for Alice: {sea}')
print(f'Bob computed key: {sb}')
print(f'Eve computed key for Bob: {seb}')
