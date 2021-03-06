import discord
import asyncio
import random
from discord.ext import commands
from time import localtime, timezone

modrole = 348838039302307840


class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='spam',
                      description='Spams a message that follow the command',
                      brief='Spams a Message')
    async def spam(self, ctx, *, msg):
        iti = 1
        while iti != 6:
            await ctx.send(msg)
            iti = iti + 1

    @commands.command(name='prunetest',
                      description='Shows how many members will be removed if server is pruned for a number of days')
    async def prunetest(self, ctx, days):
        try:
            await ctx.send(await ctx.guild.estimate_pruned_members(days=int(days)))
        except Exception as error:
            await ctx.send('ERROR: \n{}'.format(error))

    @commands.command()
    async def ping(self, ctx):
        ping = int(self.client.latency * 100)
        await ctx.send(':ping_pong: Pong! (In {}ms)'.format(str(ping)))

    @commands.command(name='changeplay',
                      description='Changes the game that the bot is playing',
                      brief='Change the Game')
    async def changeplay(self, ctx, game):
        await self.client.change_presence(game=discord.Game(name=game))
        await ctx.send("Success! I'm now playing " + game)

    @commands.command(name='cdndr',
                      description='Utility for Finding an Id for Development, Console Required',
                      brief='follow with an @mention')
    async def cdndr(self, ctx, rle):
        print(rle)
        await ctx.send('`' + rle + '`')

    @commands.command(name='timer',
                      description='Start a Timer',
                      brief='Timer')
    async def timer(self, ctx, Minutes, Seconds):
        sender = ctx.message.author.mention
        await ctx.send('Timer started for ' + Minutes + ' minutes and ' + Seconds + ' seconds.')
        time = (int(Minutes) * 60) + int(Seconds)
        await asyncio.sleep(time)
        await ctx.send('The timer set by ' + sender + ', is done')

    @commands.command(name='dale',
                      description='dale',
                      brief='dale')
    async def dale(self, ctx):
        if ctx.message.server == 333534981831917570:
            ctx.send('<@164876392494792705>, You a bitch')

    @commands.command(name='rc',
                      description='A ready Check',
                      brief='Ready Check',
                      aliases=['Readycheck', 'readycheck'])
    async def rc(self, ctx, tot):
        global ready
        global tim
        tot = int(tot)
        if tot <= 0:
            await ctx.send('You need to specify how many people we are waiting on')
        else:
            await ctx.send('Ready Check! Waiting on ' + str(tot) + 'People!' + '\n' + "Ready Up with '!r'")
            ready = 0
            tim = 0
            while ready < tot:
                if tim == (15 * 3):
                    await ctx.send("The ready check has timed out")
                    break
                tim = tim + 3
                await asyncio.sleep(3)
            if ready >= tot:
                await ctx.send('Everyone is Ready!')

    @commands.command(name='r',
                      brief='Used in a Ready Check',
                      aliases=['R'])
    async def r(self, ctx):
        global ready
        global tim
        ready = ready + 1
        tim = 0
        await ctx.send(ctx.message.author.mention + 'has readied up!')

    @commands.command(name='opt',  # FIXME Cant poll server for roles correctly
                      brief='Opt in or out for mention notifications')
    async def opt(self, ctx, inorout, entered_role):
        team_list = ["Overwatch", "Ark", "WoW"]
        entered_team = entered_role.lower()
        role = discord.utils.get(ctx.message.server.roles, name=entered_team)
        #roles = [
        #    # IDs of the roles for the teams
        #    '526447124821573642',  # Overwatch
        #    '526447129477120007',  # Ark
        #   '526447131641380885',  # Wow
        #]
        print(role.name)
        if role is None or role.name not in team_list:
            # If the role wasn't found by discord.utils.get() or is a role that we don't want to add:
            await ctx.send('Unknown role, possible roles are Overwatch, Ark, and WoW')
            return
        elif role in ctx.message.author.roles:
            # If they already have the role
            await ctx.send("You already have this role.")
        else:
            try:
                await self.client.add_roles(ctx.message.author, role)
                await self.client.send_message(ctx.message.channel, "Successfully added role {0}".format(role.name))
            except discord.Forbidden:
                await self.client.send_message(ctx.message.channel, "I don't have perms to add roles.")

    @commands.command(name='announce',
                      brief='Mods Only',
                      no_pm=True)
    async def announce(self, ctx, channel: discord.TextChannel, *, msg):
        if 'moderator' in [y.name.lower() for y in ctx.message.author.roles]:
            announcement = 'Announcement:' + '\n' + msg
            await channel.send(announcement)
        elif 'moderator' not in [y.name.lower() for y in ctx.message.author.roles]:
            ctx.send("You do not have permission to use this command")

    @commands.command(name='hello',
                      description='It is good to be polite when meeting new friends',
                      brief='Make a first impression',
                      aliases=['hi, hia, hiya'])
    async def hello(self, ctx):
        await ctx.send('Hello, ' + ctx.message.author.mention)

    @commands.command(name='time',
                      description='Returns the time of the bot',
                      brief='Bot Time')
    async def time(self, ctx):
        await ctx.send(
            'Time: ' + str(localtime().tm_hour) + ':' + str(localtime().tm_min) + '\n' + 'Timezone: ' + str(
                timezone) + '\n' + 'Daylight Savings: ' + str(localtime().tm_isdst))

    @commands.command()
    async def shutdown(self, ctx):
        await ctx.send('Sorry ' + ctx.message.author.mention + ", I can't let you do that.")

    @commands.command()
    async def makemeasandwich(self, ctx):
        await ctx.send(':hamburger:')

    @commands.command()
    async def filemytaxes(self, ctx):
        await ctx.send('No, do them yourself:' + '\n' + 'https://www.irs.gov/forms-instructions')

    @commands.command()
    async def randomcatfact(self, ctx):
        facts = [
            'Unlike dogs, cats do not have a sweet tooth. Scientists believe this is due to a mutation in a key taste receptor.',
            'When a cat chases its prey, it keeps its head level. Dogs and humans bob their heads up and down.',
            'The technical term for a cat’s hairball is a “bezoar.”',
            'A group of cats is called a “clowder.”',
            'A cat can’t climb head first down a tree because every claw on a cat’s paw points the same way. To get down from a tree, a cat must back down.',
            'Cats make about 100 different sounds. Dogs make only about 10.',
            'There are more than 500 million domestic cats in the world, with approximately 40 recognized breeds.',
            'Approximately 24 cat skins can make a coat.',
            'While it is commonly thought that the ancient Egyptians were the first to domesticate cats, the oldest known pet cat was recently found in a 9,500-year-old grave on the Mediterranean island of Cyprus. This grave predates early Egyptian art depicting cats by 4,000 years or more.',
            'During the time of the Spanish Inquisition, Pope Innocent VIII condemned cats as evil and thousands of cats were burned. Unfortunately, the widespread killing of cats led to an explosion of the rat population, which exacerbated the effects of the Black Death.',
            'During the Middle Ages, cats were associated with withcraft, and on St. John’s Day, people all over Europe would stuff them into sacks and toss the cats into bonfires. On holy days, people celebrated by tossing cats from church towers.',
            'The first cat in space was a French cat named Felicette (a.k.a. “Astrocat”) In 1963, France blasted the cat into outer space. Electrodes implanted in her brains sent neurological signals back to Earth. She survived the trip.',
            'The group of words associated with cat (catt, cath, chat, katze) stem from the Latin catus, meaning domestic cat, as opposed to feles, or wild cat.',
            'The term “puss” is the root of the principal word for “cat” in the Romanian term pisica and the root of secondary words in Lithuanian (puz) and Low German puus. Some scholars suggest that “puss” could be imitative of the hissing sound used to get a cat’s attention. As a slang word for the female pudenda, it could be associated with the connotation of a cat being soft, warm, and fuzzy.',
            'Approximately 40,000 people are bitten by cats in the U.S. annually.',
            'Cats are North America’s most popular pets: there are 73 million cats compared to 63 million dogs. Over 30% of households in North America own a cat.',
            'According to Hebrew legend, Noah prayed to God for help protecting all the food he stored on the ark from being eaten by rats. In reply, God made the lion sneeze, and out popped a cat.',
            'A cat’s hearing is better than a dog’s. And a cat can hear high-frequency sounds up to two octaves higher than a human.',
            'A cat can travel at a top speed of approximately 31 mph (49 km) over a short distance.',
            'A cat rubs against people not only to be affectionate but also to mark out its territory with scent glands around its face. The tail area and paws also carry the cat’s scent.',
            'Researchers are unsure exactly how a cat purrs. Most veterinarians believe that a cat purrs by vibrating vocal folds deep in the throat. To do this, a muscle in the larynx opens and closes the air passage about 25 times per second.',
            'When a family cat died in ancient Egypt, family members would mourn by shaving off their eyebrows. They also held elaborate funerals during which they drank wine and beat their breasts. The cat was embalmed with a sculpted wooden mask and the tiny mummy was placed in the family tomb or in a pet cemetery with tiny mummies of mice.',
            'In 1888, more than 300,000 mummified cats were found an Egyptian cemetery. They were stripped of their wrappings and carted off to be used by farmers in England and the U.S. for fertilizer.',
            'Most cats give birth to a litter of between one and nine kittens. The largest known litter ever produced was 19 kittens, of which 15 survived.',
            'Smuggling a cat out of ancient Egypt was punishable by death. Phoenician traders eventually succeeded in smuggling felines, which they sold to rich people in Athens and other important cities.',
            'The earliest ancestor of the modern cat lived about 30 million years ago. Scientists called it the Proailurus, which means “first cat” in Greek. The group of animals that pet cats belong to emerged around 12 million years ago.',
            'The biggest wildcat today is the Siberian Tiger. It can be more than 12 feet (3.6 m) long (about the size of a small car) and weigh up to 700 pounds (317 kg).',
            'A cat’s brain is biologically more similar to a human brain than it is to a dog’s. Both humans and cats have identical regions in their brains that are responsible for emotions.',
            'Many Egyptians worshipped the goddess Bast, who had a woman’s body and a cat’s head.',
            'Mohammed loved cats and reportedly his favorite cat, Muezza, was a tabby. Legend says that tabby cats have an “M” for Mohammed on top of their heads because Mohammad would often rest his hand on the cat’s head.',
            'While many parts of Europe and North America consider the black cat a sign of bad luck, in Britain and Australia, black cats are considered lucky.',
            'The most popular pedigreed cat is the Persian cat, followed by the Main Coon cat and the Siamese cat.',
            'The smallest pedigreed cat is a Singapura, which can weigh just 4 lbs (1.8 kg), or about five large cans of cat food. The largest pedigreed cats are Maine Coon cats, which can weigh 25 lbs (11.3 kg), or nearly twice as much as an average cat weighs.',
            'Some cats have survived falls of over 65 feet (20 meters), due largely to their “righting reflex.” The eyes and balance organs in the inner ear tell it where it is in space so the cat can land on its feet. Even cats without a tail have this ability.',
            'Some Siamese cats appear cross-eyed because the nerves from the left side of the brain go to mostly the right eye and the nerves from the right side of the brain go mostly to the left eye. This causes some double vision, which the cat tries to correct by “crossing” its eyes.',
            'Researchers believe the word “tabby” comes from Attabiyah, a neighborhood in Baghdad, Iraq. Tabbies got their name because their striped coats resembled the famous wavy patterns in the silk produced in this city.',
            'A cat can jump up to five times its own height in a single bound.',
            'Cats hate the water because their fur does not insulate well when it’s wet. The Turkish Van, however, is one cat that likes swimming. Bred in central Asia, its coat has a unique texture that makes it water resistant.',
            'The Egyptian Mau is probably the oldest breed of cat. In fact, the breed is so ancient that its name is the Egyptian word for “cat.”',
            'The first commercially cloned pet was a cat named "Little Nicky." He cost his owner $50,000, making him one of the most expensive cats ever.',
            'A cat usually has about 12 whiskers on each side of its face.',
            'A cat’s eyesight is both better and worse than humans. It is better because cats can see in much dimmer light and they have a wider peripheral view. It’s worse because they don’t see color as well as humans do. Scientists believe grass appears red to cats.',
            'Spanish-Jewish folklore recounts that Adam’s first wife, Lilith, became a black vampire cat, sucking the blood from sleeping babies. This may be the root of the superstition that a cat will smother a sleeping baby or suck out the child’s breath.',
            'Perhaps the most famous comic cat is the Cheshire Cat in Lewis Carroll’s Alice in Wonderland. With the ability to disappear, this mysterious character embodies the magic and sorcery historically associated with cats.',
            'The smallest wildcat today is the Black-footed cat. The females are less than 20 inches (50 cm) long and can weigh as little as 2.5 lbs (1.2 kg).',
            'On average, cats spend 2/3 of every day sleeping. That means a nine-year-old cat has been awake for only three years of its life.',
            'In the original Italian version of Cinderella, the benevolent fairy godmother figure was a cat.',
            'The little tufts of hair in a cat’s ear that help keep out dirt direct sounds into the ear, and insulate the ears are called “ear furnishings.”',
            'The ability of a cat to find its way home is called “psi-traveling.” Experts think cats either use the angle of the sunlight to find their way or that cats have magnetized cells in their brains that act as compasses.',
            'Isaac Newton invented the cat flap. Newton was experimenting in a pitch-black room. Spithead, one of his cats, kept opening the door and wrecking his experiment. The cat flap kept both Newton and Spithead happy.',
            'The world’s rarest coffee, Kopi Luwak, comes from Indonesia where a wildcat known as the luwak lives. The cat eats coffee berries and the coffee beans inside pass through the stomach. The beans are harvested from the cat’s dung heaps and then cleaned and roasted. Kopi Luwak sells for about $500 for a 450 g (1 lb) bag.',
            'A cat’s jaw can’t move sideways, so a cat can’t chew large chunks of food.',
            "Cats don't actually meow at each other, just at humans. Cats typically will spit, purr, and hiss at other cats.",
            'Female cats tend to be right pawed, while male cats are more often left pawed. Interestingly, while 90% of humans are right handed, the remaining 10% of lefties also tend to be male.',
            'A cat’s back is extremely flexible because it has up to 53 loosely fitting vertebrae. Humans only have 34.',
            'All cats have claws, and all except the cheetah sheath them when at rest.',
            'Two members of the cat family are distinct from all others: the clouded leopard and the cheetah. The clouded leopard does not roar like other big cats, nor does it groom or rest like small cats. The cheetah is unique because it is a running cat; all others are leaping cats. They are leaping cats because they slowly stalk their prey and then leap on it.',
            'A cat lover is called an Ailurophilia (Greek: cat+lover).',
            'In Japan, cats are thought to have the power to turn into super spirits when they die. This may be because according to the Buddhist religion, the body of the cat is the temporary resting place of very spiritual people.',
            'Most cats had short hair until about 100 years ago, when it became fashionable to own cats and experiment with breeding.',
            'One reason that kittens sleep so much is because a growth hormone is released only during sleep.',
            'Cats have about 130,000 hairs per square inch (20,155 hairs per square centimeter).',
            'The heaviest cat on record is Himmy, a Tabby from Queensland, Australia. He weighed nearly 47 pounds (21 kg). He died at the age of 10.',
            'The oldest cat on record was Crème Puff from Austin, Texas, who lived from 1967 to August 6, 2005, three days after her 38th birthday. A cat typically can live up to 20 years, which is equivalent to about 96 human years.',
            'The lightest cat on record is a blue point Himalayan called Tinker Toy, who weighed 1 pound, 6 ounces (616 g). Tinker Toy was 2.75 inches (7 cm) tall and 7.5 inches (19 cm) long.',
            'Approximately 1/3 of cat owners think their pets are able to read their minds.',
            'The tiniest cat on record is Mr. Pebbles, a 2-year-old cat that weighed 3 lbs (1.3 k) and was 6.1 inches (15.5 cm) high.',
            'A commemorative tower was built in Scotland for a cat named Towser, who caught nearly 30,000 mice in her lifetime.',
            'In the 1750s, Europeans introduced cats into the Americas to control pests.',
            'The first cat show was organized in 1871 in London. Cat shows later became a worldwide craze.',
            'The first cartoon cat was Felix the Cat in 1919. In 1940, Tom and Jerry starred in the first theatrical cartoon “Puss Gets the Boot.” In 1981 Andrew Lloyd Weber created the musical Cats, based on T.S. Eliot’s Old Possum’s Book of Practical Cats',
            'The normal body temperature of a cat is between 100.5 ° and 102.5 °F. A cat is sick if its temperature goes below 100 ° or above 103 °F.',
            'A cat has 230 bones in its body. A human has 206. A cat has no collarbone, so it can fit through any opening the size of its head.',
            'Cats have 32 muscles that control the outer ear (humans have only 6). A cat can independently rotate its ears 180 degrees',
            'A cat’s nose pad is ridged with a unique pattern, just like the fingerprint of a human.',
            'If they have ample water, cats can tolerate temperatures up to 133 °F.',
            'Foods that should not be given to cats include onions, garlic, green tomatoes, raw potatoes, chocolate, grapes, and raisins. Though milk is not toxic, it can cause an upset stomach and gas. Tylenol and aspirin are extremely toxic to cats, as are many common houseplants. Feeding cats dog food or canned tuna that’s for human consumption can cause malnutrition.',
            'A 2007 Gallup poll revealed that both men and women were equally likely to own a cat.',
            'A cat’s heart beats nearly twice as fast as a human heart, at 110 to 140 beats a minute.',
            'In just seven years, a single pair of cats and their offspring could produce a staggering total of 420,000 kittens.',
            'Relative to its body size, the clouded leopard has the biggest canines of all animals’ canines. Its dagger-like teeth can be as long as 1.8 inches (4.5 cm).',
            'Cats spend nearly 1/3 of their waking hours cleaning themselves.',
            'Grown cats have 30 teeth. Kittens have about 26 temporary teeth, which they lose when they are about 6 months old.',
            'Cats don’t have sweat glands over their bodies like humans do. Instead, they sweat only through their paws.',
            'A cat called Dusty has the known record for the most kittens. She had more than 420 kittens in her lifetime.',
            'The largest cat breed is the Ragdoll. Male Ragdolls weigh between 12 and 20 lbs (5.4-9.0 k). Females weigh between 10 and 15 lbs (4.5-6.8 k).',
            'Cats are extremely sensitive to vibrations. Cats are said to detect earthquake tremors 10 or 15 minutes before humans can.',
            'In contrast to dogs, cats have not undergone major changes during their domestication process.',
            'A female cat is called a queen or a molly.',
            'In the 1930s, two Russian biologists discovered that color change in Siamese kittens depend on their body temperature. Siamese cats carry albino genes that work only when the body temperature is above 98° F. If these kittens are left in a very warm room, their points won’t darken and they will stay a creamy white.',
            'There are up to 60 million feral cats in the United States alone.',
            'The oldest cat to give birth was Kitty who, at the age of 30, gave birth to two kittens. During her life, she gave birth to 218 kittens.',
            'The most traveled cat is Hamlet, who escaped from his carrier while on a flight. He hid for seven weeks behind a panel on the airplane. By the time he was discovered, he had traveled nearly 373,000 miles (600,000 km).',
            'In Holland’s embassy in Moscow, Russia, the staff noticed that the two Siamese cats kept meowing and clawing at the walls of the building. Their owners finally investigated, thinking they would find mice. Instead, they discovered microphones hidden by Russian spies. The cats heard the microphones when they turned on.',
            'The most expensive cat was an Asian Leopard cat (ALC)-Domestic Shorthair (DSH) hybrid named Zeus. Zeus, who is 90% ALC and 10% DSH, has an asking price of £100,000 ($154,000).',
            'The cat who holds the record for the longest non-fatal fall is Andy. He fell from the 16th floor of an apartment building (about 200 ft/.06 km) and survived.',
            'Rome has more homeless cats per square mile than any other city in the world.',
            'The richest cat is Blackie who was left £15 million by his owner, Ben Rea.',
            'The claws on the cat’s back paws aren’t as sharp as the claws on the front paws because the claws in the back don’t retract and, consequently, become worn.',
            'Cats can drink seawater.']
        await ctx.send(random.choice(facts))

    @commands.command(name='patchnotes',
                    brief='Patch Notes',
                    alias=['patch,changes'])
    async def patchnotes(self, ctx):
        embed = discord.Embed(
            title="Wolfbot",
            description='Patch Notes',
            colour=discord.Color.blue(),
        )
        embed.set_footer(text='Version: ' + '5')
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/467509886272667649/490365802843734037/Wolfbot_Icon.png')

        embed.add_field(name='Change', value='Description', inline=False)
        embed.add_field(name='Ready check', value='Changed timeout to reset timer after someone readies', inline=False)
        embed.add_field(name='!aroll', value='Rolls a d20 with the ability modifier of a character', inline=False)
        embed.add_field(name='Note', value='!movechan does not work', inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Utilities(client))
    print('Utilities is loaded')
