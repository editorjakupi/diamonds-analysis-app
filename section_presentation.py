"""Presentation: background, 4Cs, executive summary."""

from __future__ import annotations

import streamlit as st


def render_presentation() -> None:
    st.title("Presentation")
    st.markdown(
        """
    ### Bakgrund
    Guldfynd överväger att expandera sitt sortiment med diamanter.
    Denna analys hjälper till att förstå diamanternas egenskaper och marknadsmöjligheter.
    """
    )

    st.markdown(
        """
    ### Om diamanter

    Diamanter är en av världens mest värdefulla ädelstenar, bildade under extremt högt tryck och temperatur djupt under jordens yta.
    De består av kolatomer i en kristallstruktur och är kända för sin exceptionella hårdhet och briljans.

    #### De 4 C:na - Diamantens Viktigaste Egenskaper

    1. **Cut (Slipning)**
       - Beskriver hur väl diamanten är slipad och formad
       - Påverkar hur ljuset reflekteras och diamantens briljans
       - Kvaliteter från bäst till sämst: Ideal, Premium, Very Good, Good, Fair

    2. **Color (Färg)**
       - Mäter färglösheten i diamanten
       - Skala från D (helt färglös) till Z (ljusgul)
       - D-F: Färglösa
       - G-J: Nästan färglösa
       - K-M: Svagt färgade

    3. **Clarity (Klarhet)**
       - Beskriver frånvaron av inre och yttre brister
       - IF (Internally Flawless): Perfekt
       - VVS1-VVS2 (Very Very Slightly Included): Mycket små inneslutningar
       - VS1-VS2 (Very Slightly Included): Små inneslutningar
       - SI1-SI2 (Slightly Included): Synliga inneslutningar
       - I1-I3 (Included): Tydliga inneslutningar

    4. **Carat (Vikt)**
       - Mäter diamantens vikt
       - 1 karat = 0.2 gram
       - Större diamanter är sällsyntare och därför värdefullare

    #### Andra Viktiga Egenskaper

    - **Depth (Djup)**: Förhållandet mellan diamantens höjd och diameter
    - **Table (Tavla)**: Storleken på diamantens toppfasetter
    - **Dimensions (x, y, z)**: Diamantens fysiska mått i millimeter

    #### Värdering och Prissättning

    Diamantens värde bestäms av en kombination av alla 4 C:na, där:
    - Hög kvalitet på alla C:na ger högst värde
    - Vikt (carat) har ofta störst påverkan på priset
    - Perfekta diamanter (D-IF) är extremt sällsynta och värdefulla
    - Mindre perfekta diamanter kan erbjuda bättre värde för pengarna

    Denna kunskap är viktig för att förstå analysen och dess affärsmässiga implikationer.
    """
    )

    st.header("Executive summary och data storytelling")
    st.markdown(
        """
    ### Huvudinsikter
    1. **Marknadssegmentering**
       - Priser och kvaliteter varierar stort, men det är vikten (carat) som är den primära prisdrivande faktorn.
         _Detta innebär att prissättning bör baseras på vikt, medan kvalitetsattribut används för att skapa olika produktsegment._
    2. **Kvalitetsattribut**
       - Premium och Fair har högst medel- och medianpris för slipning, men detta beror på att dessa klasser har högst vikt.
         _Detta visar att slipningskvaliteten i sig inte är den avgörande prisfaktorn._
       - J, I och H har högst medel- och medianpris för färg, men även här är det vikten som förklarar de högre priserna.
         _Detta innebär att färgkvaliteten är en sekundär prisfaktor._
       - SI2, SI1 och I1 har högst medel- och medianpris för klarhet, vilket också förklaras av högre vikt.
         _Detta visar att klarhetsgraden i sig inte är den enda prisdrivande faktorn._
    3. **Prisdrivande faktorer**
       - Vikt (carat) är den starkaste prisdrivande faktorn, följt av kvalitetsattribut.
         _Större diamanter är betydligt dyrare, oavsett kvalitetsklass._
    4. **Extremvärden och saknade värden**
       - Extremvärden förekommer i samtliga nyckelvariabler (pris, vikt, djup, tavla) och kan snedvrida analysen, särskilt medelvärden och samband. För price kan enstaka mycket dyra diamanter ge en felaktig bild av prisnivåer. För carat kan extremt höga eller låga vikter påverka analysen av sambandet mellan vikt och pris. För depth och table kan extremvärden indikera mätfel eller ovanliga slipningar, vilket påverkar slutsatser om kvalitet och pris. Dessa bör identifieras och hanteras vid analys och affärsbeslut.
         _Datadrivna beslut kring lager och prissättning blir mer tillförlitliga om extremvärden hanteras korrekt._
    5. **Statistiska skillnader**
       - Prisskillnader mellan kvalitetsklasser är signifikanta, men till stor del förklaras av vikt.
         _Detta bekräftas av hypotesprövningar och bör beaktas vid sortimentsplanering._
    6. **Affärsmässiga implikationer**
       - Sortiment och prissättning bör primärt baseras på vikt, med kvalitetsattribut som sekundära faktorer.
         _Genom att analysera vilka viktsegment som är mest lönsamma kan man optimera utbudet._
       - Extremvärden bör identifieras och hanteras särskilt vid prissättning och sortimentsplanering, eftersom de kan vara svårsålda, påverka lönsamheten eller ge en missvisande bild av marknaden.
         _Exkludera eller särskilt analysera diamanter med extremvärden för att fatta mer tillförlitliga beslut._
       - Premiumprodukter kan marknadsföras baserat på kombinationen av vikt och kvalitet.
         _Detta möjliggör differentierad marknadsföring och ökad lönsamhet._
       - Dataanalys möjliggör datadrivna beslut för inköp, lager och kampanjer.
         _Att använda insikter från datan minskar risken för felbeslut och ökar konkurrenskraften._
    7. **Korrelationer och samband**
       - Carat och pris har starkast positiv korrelation.
         _Det är viktigt att förstå detta samband för att kunna förutsäga pris och identifiera avvikelser._
       - Måtten x, y, z är starkt korrelerade med vikt.
         _Detta visar att diamantens dimensioner hänger ihop med vikt och kan användas för kvalitetskontroll._
    8. **Kundperspektiv**
       - Det finns "fyndmöjligheter" i vissa viktsegment.
         _Kunder med kunskap kan hitta diamanter med bra värde genom att fokusera på vikt och kompromissa på vissa kvalitetsattribut._
    9. **Storytelling**
       - Diamantmarknaden är bred och mångfacetterad, med både exklusiva och prisvärda alternativ.
         _Analysen visar att det finns utrymme för både lyx och volym, och att datadrivna beslut kan maximera värdet för både företag och kund._

    ### Rekommendationer
    - Basera prissättning och sortimentsplanering primärt på vikt (carat).
      _Använd kvalitetsattribut som sekundära differentieringsfaktorer._
    - Identifiera och analysera extremvärden noggrant. Överväg att exkludera eller särskilt hantera diamanter med extremvärden vid prissättning och sortimentsplanering.
      _Detta minskar risken för felaktiga beslut och ökar lönsamheten._
    - Skapa tydliga produktsegment baserade på vikt och kvalitet.
      _Kombinera vikt med kvalitetsattribut för att skapa attraktiva erbjudanden._
    - Analysera och hantera extremvärden i lager och prissättning.
      _Undvik att låta outliers påverka prissättning och lagerbeslut._
    - Använd datadrivna insikter för att optimera utbud och lönsamhet.
      _Fortsätt analysera data löpande för att anpassa strategin till marknadens förändringar._
    """
    )
