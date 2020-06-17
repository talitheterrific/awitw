# A Walk in the Woods
import random

merch_stats = [1, 0, 0, 0, 2, 3]
war_stats = [3, 1, 2, 0, 0, 0]
wiz_stats = [0, 0, 0, 3, 1, 2]


def start():
    print('You find yourself alone on a winding cobblestone street,')
    print('the woods around you humming with summer life. The only')
    print('light comes from the full moon and the lantern you carry.')
    print('Who are you, to be walking the woods this late?')
    print('1. A traveling merchant with a full wagon.')
    print('2. A wandering warrior in search of work.')
    print('3. A wastrel of a wizard on a midnight stroll.')

    choice = input('> ')
    pick(choice)

def pick(choice):
    if '1' in choice:
        wagon()

    elif '2' in choice:
        lonely()

    elif '3' in choice:
        stroll()

    else:
        print('Please pick one of the above choices.')
        start()

def dead(reason):
    print(reason)
    print('YOU HAVE DIED')
    exit(0)

def wagon():
    print('You continue along on your rickety cart, bumping across the')
    print('stones. The horses are tired - and, frankly, so are you - but')
    print('the next town is only a few miles away. The horses clop wearily,')
    print('and you, blinking, continue to drive them.')
    luck = input('Press Enter to roll.')
    luck = random.randint(1, 20)
    luck = int(input('Input Luck for Testing Purposes: '))

    if luck < 10:
        breakdown(luck) # change how bad the break is based on luck?
    else:
        wcb(luck) # wcb = wagon chase buildup

def breakdown(luck):
    print(luck)
    if luck <= 5:
        print('With the thunderous sound of half-rotten wood snapping, the')
        print('wagon lurches, a wheel spiraling away. The horses whinny and')
        print('slow abruptly, and you barely hang on in your seat. As soon as')
        print('you hop down to check the damage, you are certain that there is')
        print('no chance of you fixing this on your own. Do you set up camp?')
        print('1. Set up camp.')
        print('2. Try and walk to town.')
        action = input('> ')

        if action == '1':
            camp()
        elif action == '2':
            footchase() # change from instant death
        else:
            print('Please input a valid response.')
            breakdown(luck)

    else:
        print('The wagon suddenly lurches with a mighty cracking sound. The')
        print('horses neigh as the structure shudders and slowly comes to a')
        print('stop. You hop off, looking at the shattered wheel. You\'ve had')
        print('to repair one of these once or twice before, but this one seems')
        print('more severe. Do you try and fix it, or set up a small camp?')
        print('1. Try to fix the wagon.')
        print('2. Set up camp.')
        action = input('> ')

        if action == '1':
            repair()
        elif action == '2':
            camp()

def camp():
    print('filler text')
    # todo: stuff for the setting up of a camp
    # todo: going to sleep
    # todo: waking up to the horses freaking out
    # todo: go to ww_desc() [werewolf description]

def footchase():
    print('filler text')
    # todo: running from the werewolf
    # todo: seeing the werewolf
    # todo: go to bit_on_foot(tags = merchant)

def horsechase():
    print('filler text')
    # todo: riding away from ww
    # todo: getting caught by ww
    # todo: glancing_bite()


def wcb(luck):
    if luck > 15:
        print('The clouds and trees part up ahead, giving you more light than')
        print('you would otherwise have. The wind picks up, and with it comes')
        print('a scent. It immediately spooks the horses, who take off without')
        print('your prodding. Then the stench reaches you - like a wet dog,')
        print('fresh from the river yet still drenched in blood.')
        action = input('What do you do? ')

        if action == '1':
            chasescene()
        elif action == '2':
            slowchase()
        else:
            dead('A werewolf catches up to you, ending your night violently.')
    else:
        print('The trees part up ahead, but the clouds have moved in above and')
        print('covered the moon. The horses plod lazily in the small valley')
        print('until something starts to spook them. One rears back, the other')
        print('tries to surge forward; you hold them as best you can, until a')
        print('sound shatters the night. Something between a howl and a scream')
        print('echoes through the night and your blood runs cold.')
        print('What do you do?')
        print('1. Get the horses running -- now!')
        print('2. Stare in disbelief. It can\'t be...')
        action = input('> ')

        if action == ('1'):
            slowchase()
        else:
            dead('A werewolf catches up to you, ending your night violently.')

def repair():
    print('The wheel sags limply, several spokes broken. To repair this, you know')
    print('you\'ll have to do two things: remove the wheel and patch together')
    print('the broken spokes. What do you do?')
    print('1. Remove the wheel.')
    print('2. Repair the spokes.')
    action = input('> ')

    if action == '1':
        jack()
    elif action == '2':
        print('You\'ll have to take the wheel off first.')
        repair()
    else:
        print('Please enter a valid response.')
        repair()

def jack():
    print('You asses the situation, and know that first you have to get the')
    print('weight of the cart off of the wheel. A collection of rocks and stone')
    print('could do the trick... of course, that means finding them first.')
    luck = input('Press Enter to Roll.')
    luck = random.randint(1, 20)
    print(luck)
    luck = int(input('Input Luck for Testing Purposes: '))

    if luck < 10:
        print('Finding enough material to lift the cart is no mean feat, and')
        print('it takes you the better part of an hour. You unhitch the horses,')
        print('tying them to a nearby tree before you start wandering the woods.')
        print('')
        print('It takes some time to find what you need, but eventually you do')
        print('find it.')
        print('It is well past midnight now, what will you do?')
        print('1. Repair the spokes.')
        print('2. Set up camp.')
        action = input('> ')


        if action == '1':
            spoke()
        else:
            dead('Your campsite is found by a group of travelers the next morning,\nits contents unspeakable in their carnage.')

def lonely():
    print('You trudge along on foot, the lantern swinging quietly in tandem')
    print('with your steps. Placeholder Text.')
    luck = input('Press Enter to roll.')
    luck = random.randint(1, 20)
    luck = int(input('Input Luck for Testing Purposes: '))

    if luck <= 5:
        werewolf(luck)
    elif luck > 5 and luck < 13:
        bear(luck)
    else:
        bandits(luck)

def bandits(luck):
    print('Three men block your path! "You\'re out late, aren\'t ya?" one')
    print('says as the other two draw knives.')
    action = input()
    if action == '1':
        combat(3, 20, 50, 'bandits')
    elif action == '2':
        bandit_talks
    else:
        print('Please input a valid response.')
        bandits(luck)

def bear(luck):
    print('A bear blocks your path!')
    combat(1, 20, 50, 'bear')

def werewolf(luck):
    print('A werewolf blocks your path!')
    combat(1, 100, 50, 'werewolf')

def victory(tags):
    print('Filler text.')

def flee(tags):
    print('You are fleeing.')
    if 'bear' in tags:
        print('You are fleeing from a bear.')
    elif 'werewolf' in tags:
        print('You are fleeing from a werewolf.')
    elif 'bandits' in tags:
        print('You are fleeing from a group of bandits.')
    else:
        print('Why are you running?')

def combat(x, ehp, php, tags):
    enemy = int(x)
    enemy_hp = int(ehp)
    player_hp = int(php)
    player_attack = random.randint(1, 20) + war_stats[0]
    print(player_attack)
    if enemy_hp <= 0:
        enemy -= 1
        enemy_hp = 20
        if enemy != 0:
            enemy_combat(enemy, enemy_hp, player_hp, tags)
        if enemy == 0:
            victory(tags)
    elif player_attack >= 13:
        print('Hit!')
        enemy_hp -= random.randint(1, 10)
        print(enemy_hp, enemy)
        run = input('Press Enter to Continue or type \'Run\' to flee!')
        if 'run' in run or 'Run' in run:
            flee(tags)
        else:
            enemy_combat(enemy, enemy_hp, player_hp, tags)

    else:
        print('Miss!')
        run = input('Press Enter to Continue or type \'Run\' to flee!')
        if 'run' in run or 'Run' in run:
            flee(tags)
        else:
            enemy_combat(enemy, enemy_hp, player_hp, tags)

def enemy_combat(x, ehp, php, tags):
    enemy = int(x)
    enemy_hp = int(ehp)
    player_hp = int(php)
    enemy_attack = random.randint(1, 20) + war_stats[0]
    print(enemy_attack)
    if player_hp <= 0:
        dead('You are mugged and left to bleed.')
    elif enemy_attack >= 13:
        print('You have been hit!')
        player_hp -= random.randint(1, 10)
        print(player_hp)
        run = input('Press Enter to Continue or type \'Run\' to flee!')
        if 'run' in run or 'Run' in run:
            flee(tags)
        else:
            combat(enemy, enemy_hp, player_hp, tags)

    else:
        print('The enemy missed!')
        run = input('Press Enter to Continue or type \'Run\' to flee!')
        if 'run' in run or 'Run' in run:
            flee(tags)
        else:
            combat(enemy, enemy_hp, player_hp, tags)

def stroll():
    print('Ah, such a lovely evening for a stroll. The full moon provides just')
    print('enough light to show the mist moving between the trees, and your')
    print('lantern\'s glow casts an eerie aura about the boughs. \'But of course,\'')
    print('you think to yourself, \'this is no mere walk! I\'m out here to do')
    print('something important!\' What was it again?')
    print('1. Summon a familiar and bond with it.')
    print('2. Enchant a wonderous amulet that will close even the gravest of wounds.')
    print('3. Build a little hut.')
    action = input('> ')

    if action == '1':
        familiar(familiar)
    elif action == '2':
        enchantment(enchantment)
    elif action == '3':
        hut(hut)
    else:
        print('Please input a valid response.')
        stroll()

def familiar(tags):
    print('Ritual text')

    disruption(tags)

def enchantment(tags):
    print('Ritual text')

    disruption(tags)

def hut(tags):
    print('Ritual text')

    disruption(tags)

def disruption(tags):
    ritual_tag = str(tags)
    if 'familiar' in ritual_tag:
        print('this works')
        explosion(ritual_tag)
    elif 'enchantment' in ritual_tag:
        print('this also works')
        explosion(ritual_tag)
    elif 'hut' in ritual_tag:
        print('this works too')
        explosion(ritual_tag)
    else:
        print('Error')

def explosion(tags):
    # print(tags)
    tags = list(tags)
    ritualtag = tags[10:-23]
    ritualtag = ''.join(ritualtag)
    print(f'The {ritualtag} explodes, sending shards of shrapnel at both you')
    print('and your foe.')

start()
