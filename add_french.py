import json

# Load existing words
with open('data/words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# Comprehensive French translations
translations = {
    # Animals
    'Cow': 'Bœuf', 'Bird': 'Oiseau', 'Cat': 'Chat', 'Chicken': 'Poulet', 
    'Dog': 'Chien', 'Crocodile': 'Crocodile', 'Moose': 'Souris', 'Sheep': 'Mouton', 
    'Pig': 'Porc', 'Rat': 'Rat', 'Turtle': 'Tortue', 'Goat': 'Chèvre',
    
    # Objects
    'Plate': 'Assiette', 'Bottle': 'Bouteille', 'Pot': 'Casserole', 'Hat': 'Chapeau', 
    'Chair': 'Chaise', 'Shoes': 'Chaussures', 'Knife': 'Couteau', 'Spoon': 'Cuillère', 
    'Bowl': 'Cuvette', 'Shirt': 'Haut', 'Bed': 'Lit', 'Book': 'Livre', 'House': 'Maison', 
    'Basket': 'Panier', 'Bag': 'Sac', 'Table': 'Table', 'Cup': 'Tasse', 
    'Telephone': 'Téléphone', 'Banana': 'Banane', 'Door': 'Porte',
    
    # Nature
    'Tree': 'Arbre', 'Path': 'Chemin', 'Sky': 'Ciel', 'Hill': 'Colline', 'Rope': 'Corde',
    'Star': 'Étoile', 'Fire': 'Feu', 'Leaf': 'Feuille', 'Forest': 'Forêt', 'Grass': 'Herbe',
    'Moon': 'Lune', 'Mountain': 'Montagne', 'Cloud': 'Nuage', 'Rock': 'Pierre', 'Rain': 'Pluie',
    'River': 'Rivière', 'Road': 'Route', 'Sun': 'Soleil', 'Soil': 'Terre', 'Wind': 'Vent', 'Water': 'Eau',
    
    # Verbs
    'To help': 'Aider', 'To like': 'Aimer', 'To bring': 'Apporter', 'To learn': 'Apprendre',
    'To wait': 'Attendre', 'To have': 'Avoir', 'To drink': 'Boire', 'To start': 'Commencer',
    'To run': 'Courir', 'To say': 'Dire', 'To give': 'Donner', 'To sleep': 'Dormir',
    'To listen': 'Entendre', 'To be': 'Être', 'To do': 'Faire', 'To close': 'Fermer',
    'To finish': 'Finir', 'To play': 'Jouer', 'To eat': 'Manger', 'To walk': 'Marcher',
    'To put': 'Mettre', 'To speak': 'Parler', 'To leave': 'Partir', 'To carry': 'Porter',
    'To come back': 'Revenir', 'To sit': "S'asseoir", 'To know': 'Savoir', 'To stand up': 'Se lever',
    'To wake up': 'Se réveiller', 'To work': 'Travailler', 'To find': 'Trouver', 'To use': 'Utiliser',
    'To come': 'Venir', 'To see': 'Voir', 'To want': 'Vouloir', 'To open': 'Ouvrir', 'To think': 'Penser',
    
    # Adjectives
    'Bitter': 'Amer', 'Good': 'Bon', 'Hot': 'Chaud', 'Short': 'Court', 'Hard': 'Dur',
    'Cold': 'Froid', 'Big': 'Grand', 'Long': 'Long', 'Bad': 'Mauvais', 'New': 'Nouveau',
    'Clean': 'Propre', 'Dirty': 'Sale', 'Dry': 'Sec', 'Dark': 'Sombre', 'Strong': 'Fort',
    'Sweet': 'Sucré', 'Empty': 'Vide', 'Open': 'Ouvert', 'Big/Tall': 'Grand',
    
    # Phrases
    'See you later': 'À plus tard', 'Help me': 'Aide-moi', 'Good morning': 'Bonjour',
    'Welcome': 'Bienvenue', "It's finished": "C'est fini", "It's not good": "C'est pas bon",
    'How are you': 'Comment ça va', 'Sorry': 'Désolé', 'Sleep well': 'Dors bien',
    "I'm hungry": "J'ai faim", "I'm thirsty": "J'ai soif", 'I like this': "J'aime ça",
    "I don't like this": "Je n'aime pas ça", 'Thanks': 'Merci', 'No': 'Non', 'Yes': 'Oui',
    'Please': "S'il te plaît", 'Wait': 'Attends', 'Go over there': 'Va là-bas', 'Come here': 'Viens ici',
    'Good morning': 'Bonjour', "It's good": "C'est bon", 'Okay': "D'accord"
}

# Add French translations to each word
for word in words:
    en_value = word.get('en', '')
    word['fr'] = translations.get(en_value, en_value)

# Save updated words
with open('data/words.json', 'w', encoding='utf-8') as f:
    json.dump(words, f, indent=2, ensure_ascii=False)

print(f'Successfully added French translations to {len(words)} words')
