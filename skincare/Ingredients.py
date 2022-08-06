from bs4 import BeautifulSoup
import requests
from csv import writer

url='https://www.byrdie.com/skincare-ingredients-glossary-4800556'
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('div',class_= "comp l-container alphabetical-list")

with open('IngredientList.csv','w', encoding= 'utf8', newline='')as f:
    thewriter = writer(f)
    header = ['ActiveIngredients']
    thewriter.writerow(header)
    for list in lists:
        title = list.find('ul', class_="alphabetical-list__list").text
        thewriter.writerow(title)

skin = pd.read_csv (r'C:\Users\flore\Downloads\skincare\cosmetics.csv')
display(skin.sample(5))

Senstitive= skin[skin["Sensitive"]==1]
Senstitive.reset_index(drop=True)
skin

Senstitive.drop(['Brand','Price','Rank','Combination','Normal','Oily','Dry'],axis=1)
NewSenSkin = NewSen.values.tolist('Ingredients')
count = 0

while (count < len(NewSenSkin)):
    print (NewSenSkin)
    count = count+1 