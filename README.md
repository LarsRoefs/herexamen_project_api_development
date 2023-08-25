<h1>Herexamen Project voor het vak API Development</h1>
<p>Welkom op mijn Github repository die ik gebruik voor het herexamen project voor het van API Development. Het project omvat een API die ik gehost heb staan op Okteto te bereiken met volgende link: https://system-service-larsroefs.cloud.okteto.net/.</p>
<p>Als thema voor mijn API heb ik gekozen voor Formule 1. Ik moest minstens 3 entiteiten voorzien, ik heb als eerst de 'users' gemaakt. Daarnaast heb ik dan nog een eintiteit gemaakt voor de f1 teams en een andere voor de f1 coureurs. Ik heb gekozen om mijn API engelstalig te maken aangezien ik dit handiger vond met naamgeving. Voor het project moesten we minstens 3 GET, 1POST, 1PUT en 1 DELETE eindepoints voorzien. Deze heb ik dan ook voorzien en meer. Om een eenvoudig een overzicht te kunnen bekijken van al deze eindpoints kan uw volgende link volgen naar OpenAPI docs van de API: https://system-service-larsroefs.cloud.okteto.net/docs#/</p>
<p>Een andere vereiste was ook het implementeren van hashing en OAuth wat dan ook natuurlijk voorzien is in mijn API. Ook heb ik gebruik gemaakt van een dockercontainer die automatisch door GitHub Actions opgebouwd wordt zoals gevraagd. Zoals eerder vermeld staat de API container dan ook Okteto cloud te draaien via Docker compose</p>
<p>Als aanvulling van het project heb ik gekozen voor de front-end omdat daar meer mijn interrese lag. Ik heb dus 3.1 gevolgd door al mijn GET en POST eindpoints te implementeren in mijn frontend applicatie. Hiervoor heb ik AlpineJS gebruikt, deze applicatie staat ook op Netlify gehost. Deze is te bereiken via volgende link: https://voluble-raindrop-dbb0f3.netlify.app. Ik heb dit kunnen realiseren door alles van mijn frontend op GitHub te zetten in een andere repository en die te gebruiken op Netlify. Alles wat in die repository te vinden is staat in deze repository onder de map 'frontend' of uw kan volgende link volgen naar de repositry: https://github.com/LarsRoefs/herexamen_API_frontend . Hiermee ben ik dus ook gegeaan voor aanvulling 3.1.1. Ik heb ook een template gebruikt en die dan angepast naar mijn wensen op de front-end dan ook leuk mogelijk te maken en dan ook voor aanvulling 3.1.2 te gaan. Verder ben ik niet gegaan met aanvullingen.</p>
<br>
<h1>Screenshots OpenAPI docs</h1>

![OpenAPIdocs1](https://drive.google.com/uc?export=view&id=1njpqlGGowTSTsLIBKxK6iudZFqbwLyPt)
![OpenAPIdocs2](https://drive.google.com/uc?export=view&id=1MPA538JUUWahw2BSUyfnUds9hjs15Juq)
![OpenAPIdocs3](https://drive.google.com/uc?export=view&id=1ISgaDcL97mJPE_9SV3JD7EVMWSH-xube)

<h1>Screenshots & Werking API Postman</h1>
<h3>POST User</h3>
<p>Als eerste moet je een user maken voor zo authenticatie te kunnen krijgen om toegang te krijgen tot de rest van de API. We maken dus een POST request naar onze API/users/. Hierin geven we 2 variabelen mee die nodig zijn voor de gerbuiker aan te maken. Namelijk email en password. Deze kan je best onthouden.</p>
![POSTUser](https://drive.google.com/uc?export=view&id=1bLoafsoAIbz3_Gea4kMClYhJ0e95sa-x)

<h3>POST Token</h3>
<p>Nu hebben we de inloggegevens nodig van de gebruiker die we net hebben aangemaakt. Deze gaan we nodig hebben voor onze bearer token te krijgen. Deze kunnen we verkijgen door een POST request naar onze API/token te maken met de inloggegevens. Als we deze dan hebben, voegen we die ook toe in de header.</p>
![POSTToken1](https://drive.google.com/uc?export=view&id=1UvQkhqlYrqerGyxMpoPyRkeYUAQDvs-v)
![POSTToken2](https://drive.google.com/uc?export=view&id=1FQAUWmmZJzl-0wAHlN_TBSRo3HWu9o8K)
