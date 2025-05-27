# Import required library for JSON handling
import json
from ipywidgets import widgets, Layout, VBox
import pandas as pd
from IPython.display import display

# Create the notebook structure with cells
notebook = {
    "cells": [
        # Title and table of contents
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Kunskapskontroll - Python och Dataanalys\n",
                "\n",
                "## Innehåll\n",
                "1. [Del 1 - Teoretiska frågor och Python-övningar](#del-1)\n",
                "2. [Del 2 - Dataanalys av Diamonds Dataset](#del-2)\n",
                "3. [Självutvärdering](#självutvärdering)"
            ]
        },
        # Part 1 header
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Del 1 - Teoretiska frågor och Python-övningar <a name=\"del-1\"></a>"
            ]
        },
        # Tuple vs List explanation
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 1. Tuple vs List\n",
                "\n",
                "Skillnaden mellan tuple och list:\n",
                "- Tuple är oföränderlig (immutable), list är föränderlig (mutable)\n",
                "- Tuple används för data som inte ska ändras, list för data som kan ändras\n",
                "- Tuple är snabbare och tar mindre minne\n",
                "- List har fler inbyggda metoder för manipulation\n",
                "\n",
                "Ingen är \"bättre\" - de har olika användningsområden:\n",
                "- Tuple: När data inte ska ändras (t.ex. koordinater, konstanter)\n",
                "- List: När data behöver manipuleras (t.ex. dynamiska samlingar)"
            ]
        },
        # Functions explanation
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 2. Funktioner\n",
                "\n",
                "Funktioner är återanvändbara kodblock som:\n",
                "- Ökar kodens läsbarhet\n",
                "- Minskar duplicering\n",
                "- Gör koden mer underhållbar\n",
                "- Möjliggör återanvändning av kod"
            ]
        },
        # Classes explanation
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 3. Klasser\n",
                "\n",
                "a) Instans: Ett konkret objekt skapat från en klass\n",
                "b) Attribut: Egenskaper/variabler som tillhör en klass\n",
                "c) Metod: Funktioner som tillhör en klass"
            ]
        },
        # Streamlit explanation
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 4. Streamlit\n",
                "\n",
                "Streamlit är ett Python-bibliotek för att skapa webbapplikationer för dataanalys.\n",
                "Det gör det enkelt att:\n",
                "- Skapa interaktiva visualiseringar\n",
                "- Bygga dashboards\n",
                "- Presentera dataanalys\n",
                "- Skapa interaktiva datamodeller"
            ]
        },
        # BankAccount class implementation
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 5. BankAccount klass"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Define the BankAccount class with basic banking operations\n",
                "class BankAccount:\n",
                "    def __init__(self, account_holder, balance=0):\n",
                "        self.account_holder = account_holder  # Store account holder name\n",
                "        self.balance = balance  # Initialize balance\n",
                "    \n",
                "    def deposit(self, amount):\n",
                "        # Add money to account if amount is positive\n",
                "        if amount > 0:\n",
                "            self.balance += amount\n",
                "            return f\"Deposited {amount}. New balance: {self.balance}\"\n",
                "        return \"Invalid amount\"\n",
                "    \n",
                "    def withdraw(self, amount):\n",
                "        # Remove money from account if sufficient balance\n",
                "        if amount > 0:\n",
                "            if amount <= self.balance:\n",
                "                self.balance -= amount\n",
                "                return f\"Withdrawn {amount}. New balance: {self.balance}\"\n",
                "            return \"Too low balance\"\n",
                "        return \"Invalid amount\"\n",
                "\n",
                "# Test the BankAccount class with example operations\n",
                "account = BankAccount(\"John Doe\", 1000)\n",
                "print(f\"Account holder: {account.account_holder}\")\n",
                "print(f\"Initial balance: {account.balance}\")\n",
                "print(account.deposit(500))\n",
                "print(account.withdraw(200))\n",
                "print(account.withdraw(2000))  # Should show \"Too low balance\""
            ]
        },
        # Vowel counter implementation
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 6. Vokalräknare"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Function to count vowels in a text string\n",
                "def vowel_checker(text):\n",
                "    vowels = \"AEIOUYÅÄÖ\"  # Define vowels including Swedish characters\n",
                "    return sum(1 for char in text.upper() if char in vowels)  # Count vowels\n",
                "\n",
                "# Test the function with a Swedish word\n",
                "print(vowel_checker(\"hjärna\"))  # Should return 2"
            ]
        },
        # Common elements implementation
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 7. Gemensamma element"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Function to find common elements between two lists\n",
                "def common_elements(list1, list2):\n",
                "    return [x for x in list1 if x in list2]  # List comprehension for common elements\n",
                "\n",
                "# Test the function with example lists\n",
                "list1 = [4, 'apple', 10, 'hi', 3]\n",
                "list2 = [23, 'apple', 5, 9, 3]\n",
                "print(common_elements(list1, list2))  # Should return ['apple', 3]"
            ]
        },
        # Storks and birth rates analysis
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 8. Storkar och barnafödsel\n",
                "\n",
                "Bilden visar ett spridningsdiagram med rubriken 'The Relationship Between Stork Populations and Human Birth Rates'. På x-axeln visas antalet storkpar ('Number of stork breeding pairs') och på y-axeln antalet födslar per år i tusental ('Birth rate (thousands per year)'). Varje punkt i grafen representerar en observation där både antalet storkpar och födelsetal har mätts. Det framgår dock inte exakt om en observation motsvarar en region, ett land, en stad eller något annat geografiskt område – men i liknande exempel brukar det ofta handla om olika regioner eller länder. Det finns en positiv trendlinje, vilket innebär att högre antal storkpar ofta sammanfaller med högre födelsetal.\n",
                "\n",
                "Slutsats:\n",
                "\n",
                "Trots att grafen visar en korrelation mellan antalet storkpar och födelsetal, innebär det inte att det finns ett orsakssamband mellan dessa två variabler. Detta är ett klassiskt exempel på en falsk korrelation (spurious correlation). Det är troligt att en tredje faktor, som till exempel regionens storlek eller befolkning, påverkar både antalet storkpar och antalet födslar. Grafen illustrerar tydligt att korrelation inte är detsamma som kausalitet, och att man måste vara försiktig med att dra slutsatser om orsakssamband enbart baserat på samband i data."
            ]
        },
        # Mean vs Median explanation
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 9. Medelvärde vs Median\n",
                "\n",
                "Nej, jag håller inte med Kim. Båda måtten har sina användningsområden:\n",
                "- Medelvärde: Bra för normalfördelad data utan extremvärden\n",
                "- Median: Bättre när det finns extremvärden eller skev fördelning"
            ]
        },
        # Pie chart explanation
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 10. Cirkeldiagram\n",
                "\n",
                "Cirkeldiagram används för att visa andelar av en helhet.\n",
                "Spotify-exempel: Visa fördelningen av musikgenrer bland användarna"
            ]
        },
        # Line chart explanation
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 11. Linjediagram\n",
                "\n",
                "Linjediagram används för att visa trender över tid.\n",
                "Spotify-exempel: Visa antalet dagliga lyssnare över ett år"
            ]
        },
        # Box plot explanation
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 12. Lådagram\n",
                "\n",
                "Lådagram (boxplot) används för att visa:\n",
                "- Median\n",
                "- Kvartiler\n",
                "- Extremvärden\n",
                "- Fördelning av data\n",
                "- Identifiera avvikelser"
            ]
        },
        # --- Del 2: Dataanalys av Diamonds Dataset ---
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Del 2 - Dataanalys av Diamonds Dataset <a name=\"del-2\"></a>"
            ]
        },
        # Bakgrund
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Bakgrund\n",
                "\n",
                "Guldfynd överväger att expandera sitt sortiment med diamanter. \n",
                "Denna analys hjälper till att förstå diamanternas egenskaper och marknadsmöjligheter."
            ]
        },
        # Om Diamanter
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Om Diamanter\n",
                "\n",
                "Diamanter är en av världens mest värdefulla ädelstenar, bildade under extremt högt tryck och temperatur djupt under jordens yta. \n",
                "De består av kolatomer i en kristallstruktur och är kända för sin exceptionella hårdhet och briljans.\n",
                "\n",
                "#### De 4 C:na - Diamantens Viktigaste Egenskaper\n",
                "\n",
                "1. **Cut (Slipning)**\n",
                "   - Beskriver hur väl diamanten är slipad och formad\n",
                "   - Påverkar hur ljuset reflekteras och diamantens briljans\n",
                "   - Kvaliteter från bäst till sämst: Ideal, Premium, Very Good, Good, Fair\n",
                "\n",
                "2. **Color (Färg)**\n",
                "   - Mäter färglösheten i diamanten\n",
                "   - Skala från D (helt färglös) till Z (ljusgul)\n",
                "   - D-F: Färglösa\n",
                "   - G-J: Nästan färglösa\n",
                "   - K-M: Svagt färgade\n",
                "\n",
                "3. **Clarity (Klarhet)**\n",
                "   - Beskriver frånvaron av inre och yttre brister\n",
                "   - IF (Internally Flawless): Perfekt\n",
                "   - VVS1-VVS2 (Very Very Slightly Included): Mycket små inneslutningar\n",
                "   - VS1-VS2 (Very Slightly Included): Små inneslutningar\n",
                "   - SI1-SI2 (Slightly Included): Synliga inneslutningar\n",
                "   - I1-I3 (Included): Tydliga inneslutningar\n",
                "\n",
                "4. **Carat (Vikt)**\n",
                "   - Mäter diamantens vikt\n",
                "   - 1 karat = 0.2 gram\n",
                "   - Större diamanter är sällsyntare och därför värdefullare\n",
                "\n",
                "#### Andra Viktiga Egenskaper\n",
                "\n",
                "- **Depth (Djup)**: Förhållandet mellan diamantens höjd och diameter\n",
                "- **Table (Tavla)**: Storleken på diamantens toppfasetter\n",
                "- **Dimensions (x, y, z)**: Diamantens fysiska mått i millimeter\n",
                "\n",
                "#### Värdering och Prissättning\n",
                "\n",
                "Diamantens värde bestäms av en kombination av alla 4 C:na, där:\n",
                "- Hög kvalitet på alla C:na ger högst värde\n",
                "- Vikt (carat) har ofta störst påverkan på priset\n",
                "- Perfekta diamanter (D-IF) är extremt sällsynta och värdefulla\n",
                "- Mindre perfekta diamanter kan erbjuda bättre värde för pengarna\n",
                "\n",
                "Denna kunskap är viktig för att förstå analysen och dess affärsmässiga implikationer."
            ]
        },
        # Förberedelser
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Förberedelser\n",
                "\n",
                "För att säkerställa att analysen bygger på rimliga och fysiskt möjliga värden tar vi bort alla rader där någon av dimensionerna x, y eller z är 0. \n",
                "En diamant kan inte ha noll i längd, bredd eller höjd. Om sådana värden finns i datan beror det på felregistreringar eller saknad data. \n",
                "Om vi inte tar bort dessa rader riskerar vi att få missvisande medelvärden, felaktiga samband och konstiga visualiseringar. \n",
                "Efter borttagning av dessa rader blir analysen mer tillförlitlig och slutsatserna mer relevanta för verkliga diamanter."
            ]
        },
        # Biblioteksimport och data-inläsning
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Importera bibliotek och ladda in data\n",
                "import pandas as pd\n",
                "import numpy as np\n",
                "import plotly.express as px\n",
                "import plotly.graph_objects as go\n",
                "\n",
                "# Läs in diamonds-datan\n",
                "df = pd.read_csv('../diamonds/diamonds.csv')\n",
                "# Ta bort rader där någon av dimensionerna x, y, z är 0\n",
                "zero_mask = (df[['x', 'y', 'z']] == 0).any(axis=1)\n",
                "df = df[~zero_mask].copy()\n",
                "print(f\"Dataset innehåller {len(df):,} diamanter efter borttagning av 0-värden.\")"
            ]
        },
        # Grundläggande Statistik
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 1. Grundläggande Statistik\n",
                "Syfte: Ge en överblick över datasetets storlek och grundläggande egenskaper."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Visa grundläggande statistik\n",
                "print(f'Antal diamanter: {len(df):,}')\n",
                "print(f'Medelpris: ${df[\"price\"].mean():,.2f}')\n",
                "print(f'Medelvikt: {df[\"carat\"].mean():.2f} karat')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Tolkning:** Datasetet är stort och representativt för marknaden. Medelpriset och medelvikten ger en första känsla för utbudet."
            ]
        },
        # Price analysis section
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 2. Prisanalys\nSyfte: Undersöka prisfördelningen och identifiera eventuella extremvärden."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Create price distribution histogram\n",
                "fig_price = px.histogram(df, x='price', nbins=50, title='Fördelning av Diamantpriser', labels={'price': 'Pris (USD)', 'count': 'Antal'})\n",
                "fig_price.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Histogram.\n",
                "**Hur man tolkar:** X-axeln visar prisintervall, Y-axeln antal diamanter. En toppig fördelning betyder många diamanter i det prisintervallet.\n",
                "**Tolkning:** Priserna är snedfördelade med många billigare diamanter och ett fåtal mycket dyra.\n",
                "**Insikt:** Priserna är koncentrerade till lägre nivåer, men det finns en lång svans av dyra diamanter.\n",
                "**Affärsmässig tolkning:** Guldfynd kan erbjuda både prisvärda och exklusiva diamanter för att möta olika kunders behov."
            ]
        },
        # Quality attributes section
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 3. Kvalitetsattribut (Cut, Color, Clarity)\nSyfte: Undersöka fördelningen av slipning, färg och klarhet. Alla är sorterade från bäst till sämst."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Define category orders from best to worst\n",
                "cut_order = ['Ideal', 'Premium', 'Very Good', 'Good', 'Fair']\n",
                "color_order = ['D', 'E', 'F', 'G', 'H', 'I', 'J']\n",
                "clarity_order = ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1']\n",
                "\n",
                "# Filter data to include only known categories\n",
                "df_cut = df[df['cut'].isin(cut_order)]\n",
                "df_color = df[df['color'].isin(color_order)]\n",
                "df_clarity = df[df['clarity'].isin(clarity_order)]\n",
                "\n",
                "# Create pie chart for cut quality\n",
                "fig_cut = px.pie(df_cut, names='cut', title='Fördelning av Slipningskvalitet', category_orders={'cut': cut_order})\n",
                "fig_cut.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Cirkeldiagram (pie chart) för slipningskvalitet.\n",
                "**Hur man tolkar:** Varje tårtbit visar andelen diamanter av en viss slipning.\n",
                "**Tolkning:** Ideal och Premium dominerar.\n",
                "**Insikt:** Majoriteten av diamanterna har hög slipningskvalitet.\n",
                "**Affärsmässig tolkning:** Guldfynd kan marknadsföra sitt sortiment som högkvalitativt och locka kvalitetsmedvetna kunder."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Create pie chart for color quality\n",
                "fig_color = px.pie(df_color, names='color', title='Fördelning av Färgkvalitet', category_orders={'color': color_order})\n",
                "fig_color.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Cirkeldiagram (pie chart) för färgkvalitet.\n",
                "**Hur man tolkar:** Varje tårtbit visar andelen diamanter av en viss färg.\n",
                "**Tolkning:** E, F och G är vanligast.\n",
                "**Insikt:** Sortimentet domineras av nästan färglösa diamanter (E, F, G). Det innebär att Guldfynd kan erbjuda hög kvalitet till ett mer tillgängligt pris än de allra mest färglösa (D).\n",
                "**Affärsmässig tolkning:** Guldfynd bör utgå från att det är vikten som driver priset i dessa segment. Färgkvalitet kan användas för att skapa produktsegment, men prissättningen bör i första hand baseras på vikt."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Create pie chart for clarity grades\n",
                "fig_clarity = px.pie(df_clarity, names='clarity', title='Fördelning av Klarhetsgrader', category_orders={'clarity': clarity_order})\n",
                "fig_clarity.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Cirkeldiagram (pie chart) för klarhetsgrader.\n",
                "**Hur man tolkar:** Varje tårtbit visar andelen diamanter av en viss klarhet.\n",
                "**Tolkning:** SI1 och VS2 är vanligast.\n",
                "**Insikt:** De flesta diamanter har medelhög klarhet.\n",
                "**Affärsmässig tolkning:** Guldfynd bör utgå från att det är vikten som driver priset i dessa segment. Klarhetsgrad kan användas för att skapa produktsegment, men prissättningen bör i första hand baseras på vikt."
            ]
        },
        # Add carat analysis to quality attributes
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Create histogram for carat (weight)\n",
                "fig_carat = px.histogram(df, x='carat', nbins=40, title='Fördelning av Vikt (Carat)', labels={'carat': 'Vikt (carat)', 'count': 'Antal'})\n",
                "fig_carat.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Histogram för vikt (carat).\n",
                "**Hur man tolkar:** X-axeln visar viktintervall (carat), Y-axeln antal diamanter.\n",
                "**Tolkning:** De flesta diamanter väger mindre än 1 carat, men det finns en lång svans av större stenar.\n",
                "**Insikt:** Små diamanter är vanligast, men stora diamanter är mer sällsynta och värdefulla.\n",
                "**Affärsmässig tolkning:** Guldfynd kan erbjuda ett brett sortiment av små diamanter för volymförsäljning och marknadsföra större stenar som exklusiva och sällsynta."
            ]
        },
        # Price analysis by clarity section
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 4. Prisfördelning per Kvalitetsattribut\nSyfte: Undersöka hur priset varierar beroende på kvalitetsattributen cut, color och clarity."
            ]
        },
        # Diagram och förklaring för cut
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Grupperat stapeldiagram för medel- och medianpris per slipning\n",
                "cut_order = ['Ideal', 'Premium', 'Very Good', 'Good', 'Fair']\n",
                "mean_price_cut = df.groupby('cut')['price'].mean().reindex(cut_order)\n",
                "median_price_cut = df.groupby('cut')['price'].median().reindex(cut_order)\n",
                "import plotly.graph_objects as go\n",
                "fig_bar_cut = go.Figure()\n",
                "fig_bar_cut.add_trace(go.Bar(x=cut_order, y=mean_price_cut, name='Medelpris'))\n",
                "fig_bar_cut.add_trace(go.Bar(x=cut_order, y=median_price_cut, name='Medianpris'))\n",
                "fig_bar_cut.update_layout(barmode='group', title='Medel- och Medianpris per Slipning', xaxis_title='Slipning', yaxis_title='Pris (USD)')\n",
                "fig_bar_cut.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Grupperat stapeldiagram för medel- och medianpris per slipning.\n",
                "**Hur man tolkar:** Varje stapel visar medel- eller medianpriset för en slipningsklass.\n",
                "**Tolkning:** Premium och Fair har högst medel- och medianpris.\n",
                "**Insikt:** Högre eller lägre slipningskvalitet kan ge högre pris, beroende på segment.\n",
                "**Affärsmässig tolkning:** Guldfynd kan ta ut högre pris för vissa slipningsklasser och bör analysera vilka segment som är mest lönsamma."
            ]
        },
        # Diagram och förklaring för color
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Grupperat stapeldiagram för medel- och medianpris per färg\n",
                "color_order = ['D', 'E', 'F', 'G', 'H', 'I', 'J']\n",
                "mean_price_color = df.groupby('color')['price'].mean().reindex(color_order)\n",
                "median_price_color = df.groupby('color')['price'].median().reindex(color_order)\n",
                "fig_bar_color = go.Figure()\n",
                "fig_bar_color.add_trace(go.Bar(x=color_order, y=mean_price_color, name='Medelpris'))\n",
                "fig_bar_color.add_trace(go.Bar(x=color_order, y=median_price_color, name='Medianpris'))\n",
                "fig_bar_color.update_layout(barmode='group', title='Medel- och Medianpris per Färg', xaxis_title='Färg', yaxis_title='Pris (USD)')\n",
                "fig_bar_color.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Grupperat stapeldiagram för medel- och medianpris per färg.\n",
                "**Hur man tolkar:** Varje stapel visar medel- eller medianpriset för en färgklass.\n",
                "**Tolkning:** J, I och H har högst medel- och medianpris.\n",
                "**Insikt:** Högre färgklass (J, I, H) har högre pris i detta dataset.\n",
                "**Affärsmässig tolkning:** Guldfynd kan ta ut högre pris för diamanter med dessa färger och bör analysera efterfrågan i dessa segment."
            ]
        },
        # Diagram och förklaring för clarity
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Grupperat stapeldiagram för medel- och medianpris per klarhetsgrad\n",
                "clarity_order = ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1']\n",
                "mean_price_clarity = df.groupby('clarity')['price'].mean().reindex(clarity_order)\n",
                "median_price_clarity = df.groupby('clarity')['price'].median().reindex(clarity_order)\n",
                "fig_bar_clarity = go.Figure()\n",
                "fig_bar_clarity.add_trace(go.Bar(x=clarity_order, y=mean_price_clarity, name='Medelpris'))\n",
                "fig_bar_clarity.add_trace(go.Bar(x=clarity_order, y=median_price_clarity, name='Medianpris'))\n",
                "fig_bar_clarity.update_layout(barmode='group', title='Medel- och Medianpris per Klarhetsgrad',\n",
                "                             xaxis_title='Klarhetsgrad', yaxis_title='Pris (USD)')\n",
                "fig_bar_clarity.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Grupperat stapeldiagram för medel- och medianpris per klarhetsgrad.\n",
                "**Hur man tolkar:** Varje stapel visar medel- eller medianpriset för en klarhetsklass.\n",
                "**Tolkning:** SI2, SI1 och I1 har högst medel- och medianpris.\n",
                "**Insikt:** De klarhetsgrader som har högst pris har också högst vikt, vilket visar att det är vikten som driver priset snarare än klarhetsgraden.\n",
                "**Affärsmässig tolkning:** Guldfynd bör utgå från att det är vikten som driver priset i dessa segment. Klarhetsgrad kan användas för att skapa produktsegment, men prissättningen bör i första hand baseras på vikt."
            ]
        },
        # Efter kod/markdown för medel- och medianpris per klarhetsgrad:
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Grupperat stapeldiagram för medel- och medianvikt per slipning\n",
                "cut_order = ['Ideal', 'Premium', 'Very Good', 'Good', 'Fair']\n",
                "mean_carat_cut = df.groupby('cut')['carat'].mean().reindex(cut_order)\n",
                "median_carat_cut = df.groupby('cut')['carat'].median().reindex(cut_order)\n",
                "import plotly.graph_objects as go\n",
                "fig_bar_carat_cut = go.Figure()\n",
                "fig_bar_carat_cut.add_trace(go.Bar(x=cut_order, y=mean_carat_cut, name='Medelvikt (carat)'))\n",
                "fig_bar_carat_cut.add_trace(go.Bar(x=cut_order, y=median_carat_cut, name='Medianvikt (carat)'))\n",
                "fig_bar_carat_cut.update_layout(barmode='group', title='Medel- och Medianvikt per Slipning', xaxis_title='Slipning', yaxis_title='Vikt (carat)')\n",
                "fig_bar_carat_cut.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Grupperat stapeldiagram för medel- och medianvikt per slipning.\n",
                "**Hur man tolkar:** Varje stapel visar medel- eller medianvikten för en slipningsklass.\n",
                "**Tolkning:** Premium och Fair har högst medel- och medianvikt.\n",
                "**Insikt:** De slipningsklasser som har högst pris har också högst vikt, vilket visar att det är vikten som driver priset snarare än slipningskvaliteten.\n",
                "**Affärsmässig tolkning:** Guldfynd bör utgå från att det är vikten som driver priset i dessa segment. Slipningskvalitet kan användas för att skapa produktsegment, men prissättningen bör i första hand baseras på vikt."
            ]
        },
        # Efter kod/markdown för medel- och medianvikt per slipning (cut):
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Grupperat stapeldiagram för medel- och medianvikt per färg\n",
                "mean_carat_color = df.groupby('color')['carat'].mean().reindex(color_order)\n",
                "median_carat_color = df.groupby('color')['carat'].median().reindex(color_order)\n",
                "fig_carat_color = go.Figure()\n",
                "fig_carat_color.add_trace(go.Bar(x=color_order, y=mean_carat_color, name='Medelvikt'))\n",
                "fig_carat_color.add_trace(go.Bar(x=color_order, y=median_carat_color, name='Medianvikt'))\n",
                "fig_carat_color.update_layout(barmode='group', title='Medel- och Medianvikt per Färg', xaxis_title='Färg', yaxis_title='Vikt (carat)')\n",
                "fig_carat_color.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Grupperat stapeldiagram för medel- och medianvikt per färg.\n",
                "**Hur man tolkar:** Varje stapel visar medel- eller medianvikten för en färgklass.\n",
                "**Tolkning:** J, I och H har högst medel- och medianvikt.\n",
                "**Insikt:** De färgklasser som har högst pris har också högst vikt, vilket visar att det är vikten som driver priset snarare än färgklassen.\n",
                "**Affärsmässig tolkning:** Guldfynd bör utgå från att det är vikten som driver priset i dessa segment. Färg kan användas för att skapa produktsegment, men prissättningen bör i första hand baseras på vikt."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Grupperat stapeldiagram för medel- och medianvikt per klarhetsgrad\n",
                "mean_carat_clarity = df.groupby('clarity')['carat'].mean().reindex(clarity_order)\n",
                "median_carat_clarity = df.groupby('clarity')['carat'].median().reindex(clarity_order)\n",
                "fig_carat_clarity = go.Figure()\n",
                "fig_carat_clarity.add_trace(go.Bar(x=clarity_order, y=mean_carat_clarity, name='Medelvikt'))\n",
                "fig_carat_clarity.add_trace(go.Bar(x=clarity_order, y=median_carat_clarity, name='Medianvikt'))\n",
                "fig_carat_clarity.update_layout(barmode='group', title='Medel- och Medianvikt per Klarhetsgrad', xaxis_title='Klarhetsgrad', yaxis_title='Vikt (carat)')\n",
                "fig_carat_clarity.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Grupperat stapeldiagram för medel- och medianvikt per klarhetsgrad.\n",
                "**Hur man tolkar:** Varje stapel visar medel- eller medianvikten för en klarhetsklass.\n",
                "**Tolkning:** SI2, SI1 och I1 har högst medel- och medianvikt.\n",
                "**Insikt:** De klarhetsgrader som har högst pris har också högst vikt, vilket visar att det är vikten som driver priset snarare än klarhetsgraden.\n",
                "**Affärsmässig tolkning:** Guldfynd bör utgå från att det är vikten som driver priset i dessa segment. Klarhetsgrad kan användas för att skapa produktsegment, men prissättningen bör i första hand baseras på vikt."
            ]
        },
        # 5. Samband mellan Vikt och Pris
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 5. Samband mellan Vikt och Pris\n",
                "Syfte: Undersöka hur vikt och pris samvarierar beroende på kvalitet."
            ]
        },
        # Vikt vs pris per slipning (cut)
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "fig_scatter_cut = px.scatter(df, x='carat', y='price', color='cut',\n",
                "                           category_orders={'cut': cut_order},\n",
                "                           title='Vikt vs Pris per Slipning',\n",
                "                           labels={'carat': 'Vikt (karat)', 'price': 'Pris (USD)'})\n",
                "fig_scatter_cut.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Spridningsdiagram (scatterplot) för vikt och pris per slipning.\n",
                "**Hur man tolkar:** Varje punkt är en diamant. Om punkterna bildar ett mönster (t.ex. stigande linje) finns ett samband. Färg visar slipning.\n",
                "**Tolkning:** Högre vikt och bättre slipning ger högre pris.\n",
                "**Insikt:** Det finns ett tydligt samband mellan vikt, slipning och pris.\n",
                "**Affärsmässig tolkning:** Guldfynd kan använda denna kunskap för att prissätta större och bättre slipade diamanter högre."
            ]
        },
        # Vikt vs pris per färg (color)
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "fig_scatter_color = px.scatter(df, x='carat', y='price', color='color',\n",
                "                             category_orders={'color': color_order},\n",
                "                             title='Vikt vs Pris per Färg',\n",
                "                             labels={'carat': 'Vikt (karat)', 'price': 'Pris (USD)'})\n",
                "fig_scatter_color.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Spridningsdiagram (scatterplot) för vikt och pris per färg.\n",
                "**Hur man tolkar:** Varje punkt är en diamant. Färg visar färgklass. Mönster visar samband.\n",
                "**Tolkning:** Färg påverkar priset, särskilt för större diamanter.\n",
                "**Insikt:** Premiumfärg ger högre pris, särskilt i större stenar.\n",
                "**Affärsmässig tolkning:** Guldfynd kan särskilt marknadsföra stora diamanter med hög färgkvalitet till premiumkunder."
            ]
        },
        # Vikt vs pris per klarhet (clarity) – redan finns, men säkerställ förklaring
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "fig_scatter_clarity = px.scatter(df, x='carat', y='price', color='clarity',\n",
                "                               category_orders={'clarity': clarity_order},\n",
                "                               title='Vikt vs Pris per Klarhet',\n",
                "                               labels={'carat': 'Vikt (karat)', 'price': 'Pris (USD)'})\n",
                "fig_scatter_clarity.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Spridningsdiagram (scatterplot) för vikt och pris per klarhet.\n",
                "**Hur man tolkar:** Varje punkt är en diamant. Färg visar klarhetsgrad. Mönster visar samband.\n",
                "**Tolkning:** Klarhet har störst effekt på priset för större diamanter.\n",
                "**Insikt:** Premiumklarhet i stora stenar ger högst pris.\n",
                "**Affärsmässig tolkning:** Guldfynd kan ta ut högre pris för stora diamanter med hög klarhet och rikta dem till exklusiva kunder."
            ]
        },
        # 6. Korrelationer
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 6. Korrelationer\n",
                "Syfte: Visa korrelationer mellan alla numeriska variabler i datasetet för att förstå sambanden mellan olika egenskaper."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Create correlation matrix for numerical columns\n",
                "numerical_cols = ['price', 'carat', 'depth', 'table', 'x', 'y', 'z']\n",
                "corr_matrix = df[numerical_cols].corr()\n",
                "\n",
                "# Create heatmap\n",
                "fig_heatmap = px.imshow(corr_matrix,\n",
                "                       labels=dict(color=\"Korrelation\"),\n",
                "                       x=numerical_cols,\n",
                "                       y=numerical_cols,\n",
                "                       title='Korrelationsmatris för Numeriska Variabler',\n",
                "                       color_continuous_scale='RdBu_r',\n",
                "                       aspect='auto')\n",
                "fig_heatmap.update_layout(\n",
                "    xaxis_title=\"Variabler\",\n",
                "    yaxis_title=\"Variabler\"\n",
                ")\n",
                "fig_heatmap.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Heatmap (värmekarta) för korrelationer.\n",
                "**Hur man tolkar:** Färgerna visar styrkan och riktningen av sambandet mellan variablerna. Röd = positiv korrelation, blå = negativ korrelation. Mörkare färg = starkare samband.\n",
                "**Tolkning:** Det finns starka positiva korrelationer mellan vikt (carat) och pris, samt mellan de fysiska måtten (x, y, z).\n",
                "**Insikt:** Vikt och fysiska mått är starkt relaterade till pris, medan djup och tavla har svagare samband.\n",
                "**Affärsmässig tolkning:** Guldfynd kan använda dessa samband för att förstå vilka faktorer som påverkar priset mest och optimera sitt sortiment."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Syfte: Det finns en stark korrelation mellan vikt (carat) och pris. Syftet är att visa sambandet mellan dessa på ett enkelt och tydligt sätt."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "fig_corr = px.scatter(df, x='carat', y='price', title='Samband mellan Vikt (Carat) och Pris', labels={'carat': 'Vikt (carat)', 'price': 'Pris (USD)'})\n",
                "fig_corr.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Spridningsdiagram (scatterplot) för vikt (carat) och pris.\n",
                "**Hur man tolkar:** Varje punkt är en diamant. Om punkterna bildar ett stigande mönster finns ett positivt samband.\n",
                "**Tolkning:** Det finns ett tydligt positivt samband mellan vikt (carat) och pris – ju större diamant, desto högre pris.\n",
                "**Insikt:** Vikt är den starkaste prisdrivande faktorn.\n",
                "**Affärsmässig tolkning:** Guldfynd kan använda detta samband för att prissätta större diamanter högre och identifiera attraktiva segment."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Starka Korrelationer mellan Diamantmått\n",
                "Syfte: Visa de tre starkaste sambanden mellan diamantens mått och vikt."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "fig_carat_x = px.scatter(df, x='carat', y='x', title='Samband mellan Vikt (carat) och Längd (x)', labels={'carat': 'Vikt (carat)', 'x': 'Längd (mm)'})\n",
                "fig_carat_x.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Spridningsdiagram (scatterplot) för vikt (carat) och längd (x).\n",
                "**Hur man tolkar:** Varje punkt är en diamant. Ett stigande mönster visar att större vikt ger större längd.\n",
                "**Tolkning:** Det finns ett mycket starkt positivt samband mellan vikt och längd.\n",
                "**Insikt:** Större diamanter är längre, vilket är logiskt och kan användas för kvalitetskontroll.\n",
                "**Affärsmässig tolkning:** Guldfynd kan använda detta samband för att snabbt uppskatta vikt utifrån längd vid värdering."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "fig_x_y = px.scatter(df, x='x', y='y', title='Samband mellan Längd (x) och Bredd (y)', labels={'x': 'Längd (mm)', 'y': 'Bredd (mm)'})\n",
                "fig_x_y.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Spridningsdiagram (scatterplot) för längd (x) och bredd (y).\n",
                "**Hur man tolkar:** Varje punkt är en diamant. Ett stigande mönster visar att längre diamanter också är bredare.\n",
                "**Tolkning:** Det finns ett mycket starkt positivt samband mellan längd och bredd.\n",
                "**Insikt:** Diamanter är ofta symmetriska, vilket syns i detta samband.\n",
                "**Affärsmässig tolkning:** Guldfynd kan använda detta samband för att kontrollera symmetri och kvalitet."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "fig_x_z = px.scatter(df, x='x', y='z', title='Samband mellan Längd (x) och Höjd (z)', labels={'x': 'Längd (mm)', 'z': 'Höjd (mm)'})\n",
                "fig_x_z.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Spridningsdiagram (scatterplot) för längd (x) och höjd (z).\n",
                "**Hur man tolkar:** Varje punkt är en diamant. Ett stigande mönster visar att längre diamanter tenderar att vara högre.\n",
                "**Tolkning:** Det finns ett starkt positivt samband mellan längd och höjd.\n",
                "**Insikt:** Diamanter med större längd tenderar att vara högre.\n",
                "**Affärsmässig tolkning:** Guldfynd kan använda detta samband för att identifiera proportionerliga och välformade diamanter."
            ]
        },
        # 7. Extremvärden och Saknade Värden
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 7. Extremvärden och Saknade Värden\n",
                "Syfte: Identifiera och analysera extremvärden och saknade värden i datasetet."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Extremvärden\n",
                "outliers = {}\n",
                "for col in ['price', 'carat', 'depth', 'table', 'x', 'y', 'z']:\n",
                "    Q1 = df[col].quantile(0.25)\n",
                "    Q3 = df[col].quantile(0.75)\n",
                "    IQR = Q3 - Q1\n",
                "    outliers[col] = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))].shape[0]\n",
                "\n",
                "fig_outliers = px.bar(x=list(outliers.keys()), y=list(outliers.values()), \n",
                "                     labels={'x': 'Variabel', 'y': 'Antal Extremvärden'}, \n",
                "                     title='Antal Extremvärden per Variabel')\n",
                "fig_outliers.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Stapeldiagram (bar chart) för extremvärden.\n",
                "**Hur man tolkar:** Varje stapel visar antalet extremvärden för en variabel.\n",
                "**Tolkning:** Extremvärden förekommer i samtliga nyckelvariabler (pris, vikt, djup, tavla) och kan snedvrida analysen, särskilt medelvärden och samband. För price kan enstaka mycket dyra diamanter ge en felaktig bild av prisnivåer. För carat kan extremt höga eller låga vikter påverka analysen av sambandet mellan vikt och pris. För depth och table kan extremvärden indikera mätfel eller ovanliga slipningar, vilket påverkar slutsatser om kvalitet och pris. Dessa bör identifieras och hanteras vid analys och affärsbeslut.\n",
                "**Insikt:** Datadrivna beslut kring lager och prissättning blir mer tillförlitliga om extremvärden hanteras korrekt. Extremvärden kan indikera unika möjligheter eller risker i sortimentet.\n",
                "**Affärsmässig tolkning:** Guldfynd bör identifiera och analysera extremvärden noggrant. Överväg att exkludera eller särskilt hantera diamanter med extremvärden vid prissättning och sortimentsplanering. Detta kan hjälpa till att optimera lager och öka lönsamheten."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "# Saknade värden\n",
                "null_values = df.isnull().sum()\n",
                "fig_null = px.bar(x=null_values.index, y=null_values.values, \n",
                "                  labels={'x': 'Variabel', 'y': 'Antal Saknade Värden'}, \n",
                "                  title='Antal Saknade Värden per Variabel')\n",
                "fig_null.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Stapeldiagram (bar chart) för saknade värden.\n",
                "**Hur man tolkar:** Varje stapel visar antalet saknade värden för en variabel.\n",
                "**Diagramtyp:** Grupperat stapeldiagram för medel- och medianpris per slipning.\n",
                "**Hur man tolkar:** Varje stapel visar medel- eller medianpriset för en slipningsklass.\n",
                "**Tolkning:** Premium och Fair har högst medel- och medianpris.\n",
                "**Insikt:** Högre eller lägre slipningskvalitet kan ge högre pris, beroende på segment.\n",
                "**Affärsmässig tolkning:** Guldfynd kan ta ut högre pris för vissa slipningsklasser och bör analysera vilka segment som är mest lönsamma."
            ]
        },
        # 8. Hypotesprövningar
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 8. Hypotesprövningar\n",
                "Syfte: Undersöka om diamanter med högre vikt (carat) har större spridning i pris än lättare diamanter. Vi delar diamanterna i två grupper: små (carat <= median) och stora (carat > median). Vi använder ett enkelt stapeldiagram för att visa prisvariationen."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Begreppsförklaring:** Prisvariation betyder hur mycket priserna skiljer sig åt inom en grupp. Hög variation betyder att det finns både billiga och dyra diamanter i gruppen."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "source": [
                "carat_median = df['carat'].median()\n",
                "df['carat_group'] = ['Låg vikt' if c <= carat_median else 'Hög vikt' for c in df['carat']]\n",
                "price_std = df.groupby('carat_group')['price'].std()\n",
                "fig_var = px.bar(x=price_std.index, y=price_std.values, \n",
                "                 labels={'x': 'Viktgrupp', 'y': 'Prisvariation (std)'}, \n",
                "                 title='Prisvariation för små och stora diamanter')\n",
                "fig_var.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Diagramtyp:** Stapeldiagram (bar chart) för prisvariation.\n",
                "**Hur man tolkar:** Varje stapel visar hur mycket priserna varierar inom gruppen. Hög stapel = stor variation.\n",
                "**Tolkning:** Stora diamanter har större prisvariation än små diamanter.\n",
                "**Insikt:** Priset på stora diamanter kan skilja sig mycket, beroende på andra faktorer som kvalitet och sällsynthet.\n",
                "**Affärsmässig tolkning:** Guldfynd bör vara extra noga med prissättning av stora diamanter, eftersom priset kan variera mycket även inom samma viktgrupp."
            ]
        },
        # 9. Beslutsstöd: Ska vi köpa diamanten?
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 9. Beslutsstöd: Ska vi köpa diamanten?\n",
                "Syfte: Hjälpa styrelsen att fatta datadrivna beslut om inköp av enskilda diamanter baserat på analysen ovan.\n",
                "\n",
                "Funktionen `should_buy_diamond` hjälper dig att fatta datadrivna beslut om du bör köpa en viss diamant eller inte.\n",
                "Du matar in diamantens egenskaper och får ett tydligt ja/nej-svar samt en motivering baserat på analysen ovan.\n",
                "\n",
                "**Exempel:**\n",
                "- Ja, priset är rimligt för denna vikt och kvalitet.\n",
                "- Nej, priset är för högt jämfört med liknande diamanter.\n",
                "- Nej, egenskaperna avviker från det normala (t.ex. extremvärde).\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Funktion för att fatta beslut om köp av diamant\n",
                "def should_buy_diamond(carat, cut, color, clarity, price, depth, table, x, y, z, df):\n",
                "    if carat <= 0 or price <= 0 or x <= 0 or y <= 0 or z <= 0:\n",
                "        return (\"Nej\", \"Ogiltiga värden: carat, pris och dimensioner måste vara större än 0.\")\n",
                "    # Kontrollera om egenskaperna är extremvärden\n",
                "    for col, val in zip(['carat','price','depth','table','x','y','z'], [carat,price,depth,table,x,y,z]):\n",
                "        Q1 = df[col].quantile(0.25)\n",
                "        Q3 = df[col].quantile(0.75)\n",
                "        IQR = Q3 - Q1\n",
                "        if val < (Q1 - 1.5*IQR) or val > (Q3 + 1.5*IQR):\n",
                "            return (\"Nej\", f\"{col}={val} är ett extremvärde jämfört med marknaden. Undvik köp utan manuell granskning.\")\n",
                "    # Jämför pris per carat mot median för denna kvalitet\n",
                "    ref = df.groupby(['cut', 'color', 'clarity'])[['price', 'carat']].median().reset_index()\n",
                "    ref['price_per_carat'] = ref['price'] / ref['carat']\n",
                "    ref_row = ref[(ref['cut']==cut) & (ref['color']==color) & (ref['clarity']==clarity)]\n",
                "    if not ref_row.empty:\n",
                "        ref_ppc = ref_row.iloc[0]['price_per_carat']\n",
                "        ppc = price / carat\n",
                "        if ppc > ref_ppc * 1.2:\n",
                "            return (\"Nej\", f\"Priset per carat ({ppc:.0f} USD) är mer än 20% högre än medianen för denna kvalitet ({ref_ppc:.0f} USD). Undvik köp.\")\n",
                "        elif ppc < ref_ppc * 0.7:\n",
                "            return (\"Ja\", f\"Priset per carat ({ppc:.0f} USD) är lågt jämfört med marknaden för denna kvalitet. Möjligt fynd!\")\n",
                "        else:\n",
                "            return (\"Ja\", f\"Priset per carat ({ppc:.0f} USD) är rimligt för denna kvalitet.\")\n",
                "    else:\n",
                "        return (\"Nej\", \"Kombinationen av cut, color och clarity är ovanlig i marknaden. Kräver manuell granskning.\")\n",
                "\n",
                "# Exempel på användning:\n",
                "carat = 0.7\n",
                "cut = 'Very Good'\n",
                "color = 'G'\n",
                "clarity = 'VS2'\n",
                "price = 3500\n",
                "depth = 61.5\n",
                "table = 57.0\n",
                "x = 5.7\n",
                "y = 5.7\n",
                "z = 3.5\n",
                "beslut, motivering = should_buy_diamond(carat, cut, color, clarity, price, depth, table, x, y, z, df)\n",
                "print(f'Rekommendation: {beslut}')\n",
                "print(f'Motivering: {motivering}')\n"
            ]
        },
        # 10. Executive Summary
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 10. Executive Summary och Data Storytelling\n",
                "\n",
                "#### Huvudinsikter\n",
                "1. **Marknadssegmentering**\n",
                "   - Priser och kvaliteter varierar stort, men det är vikten (carat) som är den primära prisdrivande faktorn.\n",
                "     _Detta innebär att prissättning bör baseras på vikt, medan kvalitetsattribut används för att skapa olika produktsegment._\n",
                "2. **Kvalitetsattribut**\n",
                "   - Premium och Fair har högst medel- och medianpris för slipning, men detta beror på att dessa klasser har högst vikt.\n",
                "     _Detta visar att slipningskvaliteten i sig inte är den avgörande prisfaktorn._\n",
                "   - J, I och H har högst medel- och medianpris för färg, men även här är det vikten som förklarar de högre priserna.\n",
                "     _Detta innebär att färgkvaliteten är en sekundär prisfaktor._\n",
                "   - SI2, SI1 och I1 har högst medel- och medianpris för klarhet, vilket också förklaras av högre vikt.\n",
                "     _Detta visar att klarhetsgraden i sig inte är den enda prisdrivande faktorn._\n",
                "3. **Prisdrivande faktorer**\n",
                "   - Vikt (carat) är den starkaste prisdrivande faktorn, följt av kvalitetsattribut.\n",
                "     _Större diamanter är betydligt dyrare, oavsett kvalitetsklass._\n",
                "4. **Extremvärden och saknade värden**\n",
                "   - Extremvärden förekommer i samtliga nyckelvariabler (pris, vikt, djup, tavla) och kan snedvrida analysen, särskilt medelvärden och samband. För price kan enstaka mycket dyra diamanter ge en felaktig bild av prisnivåer. För carat kan extremt höga eller låga vikter påverka analysen av sambandet mellan vikt och pris. För depth och table kan extremvärden indikera mätfel eller ovanliga slipningar, vilket påverkar slutsatser om kvalitet och pris. Dessa bör identifieras och hanteras vid analys och affärsbeslut.\n",
                "     _Datadrivna beslut kring lager och prissättning blir mer tillförlitliga om extremvärden hanteras korrekt._\n",
                "5. **Statistiska skillnader**\n",
                "   - Prisskillnader mellan kvalitetsklasser är signifikanta, men till stor del förklaras av vikt.\n",
                "     _Detta bekräftas av hypotesprövningar och bör beaktas vid sortimentsplanering._\n",
                "6. **Affärsmässiga implikationer**\n",
                "   - Sortiment och prissättning bör primärt baseras på vikt, med kvalitetsattribut som sekundära faktorer.\n",
                "     _Genom att analysera vilka viktsegment som är mest lönsamma kan man optimera utbudet._\n",
                "   - Extremvärden bör identifieras och hanteras särskilt vid prissättning och sortimentsplanering, eftersom de kan vara svårsålda, påverka lönsamheten eller ge en missvisande bild av marknaden.\n",
                "     _Exkludera eller särskilt analysera diamanter med extremvärden för att fatta mer tillförlitliga beslut._\n",
                "   - Premiumprodukter kan marknadsföras baserat på kombinationen av vikt och kvalitet.\n",
                "     _Detta möjliggör differentierad marknadsföring och ökad lönsamhet._\n",
                "   - Dataanalys möjliggör datadrivna beslut för inköp, lager och kampanjer.\n",
                "     _Att använda insikter från datan minskar risken för felbeslut och ökar konkurrenskraften._\n",
                "7. **Korrelationer och samband**\n",
                "   - Carat och pris har starkast positiv korrelation.\n",
                "     _Det är viktigt att förstå detta samband för att kunna förutsäga pris och identifiera avvikelser._\n",
                "   - Måtten x, y, z är starkt korrelerade med vikt.\n",
                "     _Detta visar att diamantens dimensioner hänger ihop med vikt och kan användas för kvalitetskontroll._\n",
                "8. **Kundperspektiv**\n",
                "   - Det finns \"fyndmöjligheter\" i vissa viktsegment.\n",
                "     _Kunder med kunskap kan hitta diamanter med bra värde genom att fokusera på vikt och kompromissa på vissa kvalitetsattribut._\n",
                "9. **Storytelling**\n",
                "   - Diamantmarknaden är bred och mångfacetterad, med både exklusiva och prisvärda alternativ.\n",
                "     _Analysen visar att det finns utrymme för både lyx och volym, och att datadrivna beslut kan maximera värdet för både företag och kund._\n",
                "\n",
                "#### Rekommendationer\n",
                "- Basera prissättning och sortimentsplanering primärt på vikt (carat).\n",
                "  _Använd kvalitetsattribut som sekundära differentieringsfaktorer._\n",
                "- Identifiera och analysera extremvärden noggrant. Överväg att exkludera eller särskilt hantera diamanter med extremvärden vid prissättning och sortimentsplanering.\n",
                "  _Detta minskar risken för felaktiga beslut och ökar lönsamheten._\n",
                "- Skapa tydliga produktsegment baserade på vikt och kvalitet.\n",
                "  _Kombinera vikt med kvalitetsattribut för att skapa attraktiva erbjudanden._\n",
                "- Analysera och hantera extremvärden i lager och prissättning.\n",
                "  _Undvik att låta outliers påverka prissättning och lagerbeslut._\n",
                "- Använd datadrivna insikter för att optimera utbud och lönsamhet.\n",
                "  _Fortsätt analysera data löpande för att anpassa strategin till marknadens förändringar._\n"
            ]
        },
        # Självutvärdering sist i notebooken (utförlig version)
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Självutvärdering <a name=\"självutvärdering\"></a>\n",
                "\n",
                "1. **Vad har varit roligast i kunskapskontrollen?**\n",
                "   - Dataanalysen och visualiseringen av diamanterna\n",
                "   - Skapandet av interaktiva visualiseringar med Streamlit\n",
                "   - Att se sambanden mellan olika attribut\n",
                "\n",
                "2. **Vilket betyg anser du att du ska ha och varför?**\n",
                "   - VG eftersom jag har:\n",
                "     - Skrivit tydlig och välstrukturerad kod\n",
                "     - Skapat en omfattande dataanalys med tydlig progression\n",
                "     - Implementerat en interaktiv Streamlit-applikation\n",
                "     - Presenterat insikter på ett professionellt sätt\n",
                "\n",
                "3. **Vad har varit mest utmanande i arbetet och hur har du hanterat det?**\n",
                "   - Att balansera detaljnivån i analysen\n",
                "   - Att välja rätt visualiseringar för att illustrera sambanden\n",
                "   - Lösning: Iterativ process med kontinuerlig förbättring"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Save the notebook to a file
with open('kunskapskontroll.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print("Jupyter Notebook har skapats: kunskapskontroll.ipynb")