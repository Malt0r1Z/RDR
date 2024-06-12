Titre du projet : Rogue Dead Redemption (RDR)

RDR est un jeu de Far West jouable sur IDLE.

Ce projet a été réalisé par LACOUTURE Anaïs, PRESSENDA Ugo et MEURILLON Alex.



Table des matières :
I. Description du projet 
II. Installation et exécution du projet
III. Difficultés rencontrées et implémentation dans le futur
IV. Crédits



###################################################################################################################
I. Description du projet

Venez découvrir le monde du Far Wast comme vous ne l'avez jamais vu. La version 1.0 du jeu vous attend sur IDLE.



Cette version vous fera vagabonder dans le monde du Western avec des monstres inédits comme les Pinkertons, tirés
de Red Dead Redemption.


Voici les différentes touches utilisables dans le jeu :

'a' : Déplacement diagonale haut gauche
'z' : Déplacement haut
'e' : Déplacement haut droit
'q' : Déplacement gauche
's' : Déplacement bas
'd' : Déplacement droite
'w' : Déplacement diagonale bas gauche
'c' : Déplacement diagonale bas droit
'i' : Affiche la description du héro
'k' : Tue le joueur 
'u' : Utilise un objet dans l'inventaire
'h' : Actions disponibles pour le héro
'b' : Affiche le nom du héro
'r' : Repos : Faites une sieste et regagnez 5 points de vie mais attention,
les monstres se rapprocheront de vous (5 tours de déplacement). Fonction utilisable qu'une fois par niveau. 
"échap" : Permet de quitter un menu de sélection (par exemple lors de l'interaction avec le Marchand)


On utilise également les nombres du pavé numérique de 0 à 9 comme :
'0' : Sélectionne l'élément de rang 0 dans l'inventaire du héro
...etc

Au cours de votre aventure, vous rencontrez de nombreux monstres, tous plus spéciales les uns que les autres.
Pour arriver à bout des monstres, des équipements comme la TNT vous permettront de les vaincre plus 
rapidement. 

Vous ne partirez pas les poches vides puisque vous possédez un sac (inventaire) avec uniquement 10 rangements 
et pas un de plus. Pour embarquez un nouvel objet, une fois le sac plein, il faut que jetez un objet sur le sol.

Votre plus fidèle allié, la bourse, vous accompagne au cours de vos niveaux. Au départ, vous possédez 10 pièces d'or.
Pour utiliser vos pièces, rendez-vous aux quelques marchands que vous rencontrerez sur la route.
Mais attention, ne vous baladez pas avec trop de pièces d'or où les voleurs viendront vous en volez quelqu'unes.

Votre barre d'expérience (XP), vous permettra de devenir plus fort. Chaque monstre tué vous donnera sa force 
en point d'expérience (chaque natif tué vous donne 4 points d'expérience). Au bout de 10 points d'expérience,
vous gagnez un niveau et vous repartez à 0 dans votre barre d'expérience.
Chaque niveau gagné vous donne un 1 point de vie maximal en plus et vous redonne tous vos points de vie.



Des effets néfastes séviront lors de votre aventure :

Taux d'alcoolémie : Au départ, le héro possède 30 d'alcoolémie. Tous les 5 déplacements, son taux 
d'alcoolémie diminue de 1. Une fois à 0, tous les 5 déplacements, il perd 1 hp. Pour remédier à ce problème,
il faut qu'il boit de la bière (voir ci-dessous pour la description) afin de regagner 5 d'alcoolémie.

Poison : Lors de la rencontre avec certains monstres, celui-ci vous empoisonne.
Tous les 5 déplacements, vos os se rongent et vous perdez 1 hp. Le seul remède effiface et scientifiquement
prouvé, les clopes. Votre esprit y redeviendra plus vif.



Le jeu est composé de multitudes de salles toutes reliées par un escalier (E).

Plusieurs équipements vous serviront durant votre péripétie :

clope (c) : Redonne 3 points de vie au héro et annule les effets du poison
Gold (o) : Permet d'acheter des objets chez le Marchand
bière (b) : Hydratez-vous grâce à cette boisson ! Il vous fait regagner 5 de taux d'alcoolémie
Potion de téléportation (T) : Potion qui téléporte le héro à coté de l'escalier
Potion spéciale (!) : Cette potion redonne 20 points de vie au héro {Disponible uniquement dans la salle du boss}



Afin de vous protéger, vous trouverez, dissimuler sous le sable, des armures :

Armure de paille (a) : Donnez vous un style avec de la paille (max 5 dommages)
Armure de cow-boy (A) : Enfiler l'armure la plus mythique de RDR (max 4 dommages)
Armure de plomb (P) : Parcourez les différentes cartes sous un soleil de plomb sans cramer !! (max 3 dommages)
Armure de diamant (A) : Protégez-vous pour affronter les plus grands monstres du Far West !! (max 2 dommages)
{Cette dernière est uniquement disponible dans la salle du boss}




Et des armes :
Bâton (h): C'est ce que le héro a trouvé en premier en arrivant dans le désert (attaque de 2 dégâts)
Pistolet (p) : Trouvez-en une et vous ressemblerez un peu plus à un vrai cowboy (attaque de 4 dégâts)
Fusil à pompe (f) : Dénichez-en une et vous aventure ne sera que plus simple ! (attaque de 6 dégâts)
TNT (T) : Découvrez la chimie derrière cette arme (attaque de 8 dégâts) 
{Cette dernière est disponible uniquement dans la salle du boss}




Enfin, que serait un jeu sans adversité et des monstres légendaires !? :

Natif (n) : Attention au poison venimeux de ce monstre (attaque de 1 degât et possède 4 hp). 
Il vous donnera un effet de poison, qui, tous les 5 déplacements, vous enlève 1 hp.
Cow-boy (W) : Affronter le monstre le plus mythique du farwest (attaque de 1 degât et possède 2 hp)
Shérif (S) : Oserez-vous affronter le shérif de Rogue Dead Redemption ?! (attaque de 2 degâts et possède 6 hp)
Loup (l) : ouhhhhhhh (attaque de 1 degât et possède 10 hp)
Dutch (d) : Ne le regardez pas dans les yeux, où sa fureur s'abattra sur vous (attaque de 3 degâts et possède 20 hp)
Voleur (. ou V) : Discret et rapide, le voleur ramassera vos pièces d'or (attaque de 1 degât et possède 6 hp).
Lorsque le voleur vous attaque, il vous vole une pièce d'or.
Pinkertons (K) : Les représentants de la loi sont intrétables, battez-les et vous gagnez la conquête du Far West
(attaque de 5 degâts et possède 30 hp) {Rencontre uniquement dans la salle du boss}



En vous baladant dans ce désert aride, si le soleil de RDR ou les monstres ne vous font pas peur, 
vous arriverez dans la salle du boss ! Tuez tous les monstres dont le boss, 
les Pinkertons, et récolter tous les éléments de la carte afin de terminer le jeu.




####################################################################################################################
II. Installation et exécution du projet


Pour lancer le jeu, sur IDLE, exécuter le fichier main.py, dans l'invite de commande, comme suit :
      py main.py
# Si vous rencontrez un problème, exécuter sur IDLE directement

Il se peut que lorsque vous exécuter le programme dans Visual Studio Code, la fenêtre de l'interface
soit réduite sur le bas de l'écran. Pour régler ce problème, vous pouvez agrandir la fênetre en l'étirant 
vers le haut.




###################################################################################################################
III. Difficultés rencontrées et implémentation dans le futur

Nous avons tous débutés la programmation orientée objet lors de ce deuxième semestre. Nous avons dû comprendre,
analyser et résoudre de nombreux problèmes lors des premiers Rogue afin d'apprendre les bases de cette nouvelle
façon de penser en python.

Lors de la composition du groupe de travail, nous nous sommes répartis les fonctions suivantes à implémenter dans 
notre jeu :

Anaïs : Point d'expérience XP, diagonales, repos, nourriture, poison
Ugo : Déplacements intelligents, diagonales, armes, armures, invisible
Alex : Déplacements intelligents, nuage de visibilité, pièges, boutiques, invisible

Pour certaines fonctions, nous avons décidés de les réaliser ensemble car leur fonctionnement est plus
complexe que d'autres et demande beaucoup de temps. Outre les attributions ci-dessus, nous nous sommes
aidés, chacuns, pour toutes les fonctions lorsque l'un avait un problème.

Un des problèmes majeurs que nous avons rencontré lors de la réalisation de ce projet est la réunification de nos
3 codes. En effet, le nom des varibales, les méthodes de classe, les nouvelles classes nous ont demandé de nombreux
efforts pour faire fonctionner toutes les fonctions implémentées.

Nous avons aussi envie, dans le futur, de finir l'interface graphique afin d'avoir une meilleure immersion.



###################################################################################################################
IV. Crédits

Ce projet a été réalisé par LACOUTURE Anaïs, PRESSENDA Ugo et MEURILLON Alex.
Nous voulions aussi remercier notre professeure de POO, Mme GIBART.

Nous laissons notre projet sous licence MIT.




###################################################################################################################
Conclusion :

Rogue Dead Redemption est un jeu developpé par une petite équipe de 3 personnes, à Biot, qui vous fera découvrir 
d'un nouvel oeil le monde du Far West. Si nous devions reprendre notre code, nous aimerions terminer l'interface
graphique.