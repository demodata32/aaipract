import aiml
import time
time.clock=time.time
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")
while True:
    input_text = input(">Human: ")
    response = kernel.respond(input_text)
    print(">Bot: "+response)


# hi.aiml
<?xml version="1.0" encoding="ISO-8859-1"?>

<aiml version="1.0.1">



<category>
<pattern>HI</pattern>
<template>
<random>
<li>Hello there!!</li>
<li>Hey</li>
</random>
</template>
</category>

<category>
<pattern>SUNDAY</pattern>
<template>the day of the week before Monday and following Saturday</template>
</category>
<category>
<pattern>MONDAY</pattern>
<template>the day of the week before Tuesday and following Sunday</template>
</category>
<category>
<pattern>TUESDAY</pattern>
<template>the day of the week before Wednesday and following Monday</template>
</category>
<category>
<pattern>WEDNESDAY</pattern>
<template>the day of the week before Thursday and following Tuesday</template>
</category>
<category>
<pattern>THURSDAY</pattern>
<template>the day of the week before Friday and following Wednesday</template>
</category>
<category>
<pattern>FRIDAY</pattern>
<template>the day of the week before Saturday and following Thursday</template>
</category>
<category>
<pattern>SATURDAY</pattern>
<template>the day of the week before Sunday and following Friday</template>
</category>



</aiml>

# std-startup.xml
<aiml version= "1.0.1" encoding="UTF-8">
      <category> 
           <pattern>LOAD AIML B</pattern>
           <template>
                 <learn>hi.aiml</learn>
            </template> 
      </category> 
</aiml>

