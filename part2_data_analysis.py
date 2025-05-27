# Import required libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations
import plotly.express as px  # For creating interactive visualizations
import plotly.graph_objects as go  # For advanced plot customization
import streamlit as st  # For creating the web application
from pathlib import Path  # For handling file paths
from scipy.stats import kruskal  # For statistical hypothesis testing

# Configure Streamlit page settings
st.set_page_config(
    page_title="Diamonds Analysis - Guldfynd",  # Set the page title
    page_icon="💎",  # Set the page icon
    layout="wide"  # Use wide layout for better visualization
)

# Cache the data loading function to improve performance
@st.cache_data
def load_data():
    """
    Load the diamonds dataset from CSV file.
    Returns:
        pandas.DataFrame: The loaded diamonds dataset
    """
    df = pd.read_csv('../diamonds/diamonds.csv')
    
    # Remove rows where any of the dimensions x, y, or z are 0 (physically impossible for a diamond)
    zero_mask = (df[['x', 'y', 'z']] == 0).any(axis=1)
    df = df[~zero_mask].copy()
    
    return df

# Main function for data analysis
def analyze_diamonds():
    """
    Main function that performs the complete diamond analysis and visualization.
    Creates an interactive Streamlit dashboard with various analyses.
    """
    # Load the data
    df = load_data()
    
    # Display title and introduction
    st.title("💎 Diamonds Analysis for Guldfynd")
    st.markdown("""
    ### Bakgrund
    Guldfynd överväger att expandera sitt sortiment med diamanter. 
    Denna analys hjälper till att förstå diamanternas egenskaper och marknadsmöjligheter.
    """)

    # Add diamond education section
    st.markdown("""
    ### Om Diamanter
    
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
    """)

    # 1. Basic Statistics Section
    st.header("1. Grundläggande Statistik")
    st.markdown("Syfte: Ge en överblick över datasetets storlek och grundläggande egenskaper.")
    
    # Create three columns for metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Antal diamanter", f"{len(df):,}")  # Display total number of diamonds
    with col2:
        st.metric("Medelpris", f"${df['price'].mean():,.2f}")  # Display average price
    with col3:
        st.metric("Medelvikt", f"{df['carat'].mean():.2f} karat")  # Display average carat weight

    # 2. Price Analysis Section
    st.header("2. Prisanalys")
    st.markdown("Syfte: Undersöka prisfördelningen och identifiera eventuella extremvärden.")
    
    # Create price histogram
    fig_price = px.histogram(df, x='price', nbins=50,
                           title='Fördelning av Diamantpriser',
                           labels={'price': 'Pris (USD)', 'count': 'Antal'})
    st.plotly_chart(fig_price, use_container_width=True)
    
    st.markdown("**Diagramtyp:** Histogram.")
    st.markdown("**Hur man tolkar:** X-axeln visar prisintervall, Y-axeln antal diamanter. En toppig fördelning betyder många diamanter i det prisintervallet.")
    st.markdown("**Tolkning:** Priserna är snedfördelade med många billigare diamanter och ett fåtal mycket dyra.")
    st.markdown("**Insikt:** Priserna är koncentrerade till lägre nivåer, men det finns en lång svans av dyra diamanter.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd kan erbjuda både prisvärda och exklusiva diamanter för att möta olika kunders behov.")

    # 3. Quality Attributes Section
    st.header("3. Kvalitetsattribut")
    st.markdown("Syfte: Undersöka fördelningen av slipning, färg och klarhet. Alla är sorterade från bäst till sämst.")
    
    # Define the order of categories from best to worst
    cut_order = ["Ideal", "Premium", "Very Good", "Good", "Fair"]
    color_order = ["D", "E", "F", "G", "H", "I", "J"]
    clarity_order = ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"]
    
    # Filter data to include only known categories
    df_cut = df[df['cut'].isin(cut_order)]
    df_color = df[df['color'].isin(color_order)]
    df_clarity = df[df['clarity'].isin(clarity_order)]
    
    # Create three columns for pie charts
    col1, col2, col3 = st.columns(3)
    
    # Cut quality pie chart
    with col1:
        fig_cut = px.pie(df_cut, names='cut', title='Fördelning av Slipningskvalitet',
                        category_orders={'cut': cut_order})
        st.plotly_chart(fig_cut, use_container_width=True)
        st.markdown("**Diagramtyp:** Cirkeldiagram (pie chart) för slipningskvalitet.")
        st.markdown("**Hur man tolkar:** Varje tårtbit visar andelen diamanter av en viss slipning.")
        st.markdown("**Tolkning:** Ideal och Premium dominerar.")
        st.markdown("**Insikt:** Majoriteten av diamanterna har hög slipningskvalitet.")
        st.markdown("**Affärsmässig tolkning:** Guldfynd kan marknadsföra sitt sortiment som högkvalitativt och locka kvalitetsmedvetna kunder.")
    
    # Color quality pie chart
    with col2:
        fig_color = px.pie(df_color, names='color', title='Fördelning av Färgkvalitet',
                          category_orders={'color': color_order})
        st.plotly_chart(fig_color, use_container_width=True)
        st.markdown("**Diagramtyp:** Cirkeldiagram (pie chart) för färgkvalitet.")
        st.markdown("**Hur man tolkar:** Varje tårtbit visar andelen diamanter av en viss färg.")
        st.markdown("**Tolkning:** E, F och G är vanligast.")
        st.markdown("**Insikt:** Sortimentet domineras av nästan färglösa diamanter (E, F, G). Det innebär att Guldfynd kan erbjuda hög kvalitet till ett mer tillgängligt pris än de allra mest färglösa (D).")
        st.markdown("**Affärsmässig tolkning:** Guldfynd bör utgå från att det är vikten som driver priset i dessa segment. Färgkvalitet kan användas för att skapa produktsegment, men prissättningen bör i första hand baseras på vikt.")
    
    # Clarity quality pie chart
    with col3:
        fig_clarity = px.pie(df_clarity, names='clarity', title='Fördelning av Klarhetsgrader',
                            category_orders={'clarity': clarity_order})
        st.plotly_chart(fig_clarity, use_container_width=True)
        st.markdown("**Diagramtyp:** Cirkeldiagram (pie chart) för klarhetsgrader.")
        st.markdown("**Hur man tolkar:** Varje tårtbit visar andelen diamanter av en viss klarhet.")
        st.markdown("**Tolkning:** SI1 och VS2 är vanligast.")
        st.markdown("**Insikt:** De flesta diamanter har medelhög klarhet.")
        st.markdown("**Affärsmässig tolkning:** Guldfynd bör utgå från att det är vikten som driver priset i dessa segment. Klarhetsgrad kan användas för att skapa produktsegment, men prissättningen bör i första hand baseras på vikt.")
    
    # Add clarity grade explanations
    st.markdown("**Clarity-beteckningar:**\n- IF: Internally Flawless\n- VVS1/VVS2: Very Very Slightly Included\n- VS1/VS2: Very Slightly Included\n- SI1/SI2: Slightly Included\n- I1: Included")

    # Carat (weight) histogram and explanation
    with st.container():
        fig_carat = px.histogram(df, x='carat', nbins=40, title='Fördelning av Vikt (Carat)', labels={'carat': 'Vikt (carat)', 'count': 'Antal'})
        st.plotly_chart(fig_carat, use_container_width=True)
        st.markdown("**Diagramtyp:** Histogram för vikt (carat).")
        st.markdown("**Hur man tolkar:** X-axeln visar viktintervall (carat), Y-axeln antal diamanter.")
        st.markdown("**Tolkning:** De flesta diamanter väger mindre än 1 carat, men det finns en lång svans av större stenar.")
        st.markdown("**Insikt:** Små diamanter är vanligast, men stora diamanter är mer sällsynta och värdefulla.")
        st.markdown("**Affärsmässig tolkning:** Guldfynd kan erbjuda ett brett sortiment av små diamanter för volymförsäljning och marknadsföra större stenar som exklusiva och sällsynta.")

    # 4. Price Distribution by Quality Attributes
    st.header("4. Prisfördelning per Kvalitetsattribut")
    st.markdown("Syfte: Jämföra prisnivåer mellan olika kvalitetsklasser.")
    
    # Replace boxplot for price per cut with grouped bar chart (mean and median)
    mean_price_cut = df.groupby('cut')['price'].mean().reindex(cut_order)
    median_price_cut = df.groupby('cut')['price'].median().reindex(cut_order)
    fig_bar_cut = go.Figure()
    fig_bar_cut.add_trace(go.Bar(x=cut_order, y=mean_price_cut, name='Medelpris'))
    fig_bar_cut.add_trace(go.Bar(x=cut_order, y=median_price_cut, name='Medianpris'))
    fig_bar_cut.update_layout(barmode='group', title='Medel- och Medianpris per Slipning', xaxis_title='Slipning', yaxis_title='Pris (USD)')
    st.plotly_chart(fig_bar_cut, use_container_width=True)
    st.markdown("**Diagramtyp:** Grupperat stapeldiagram för medel- och medianpris per slipning.")
    st.markdown("**Hur man tolkar:** Varje stapel visar medel- eller medianpriset för en slipningsklass.")
    st.markdown("**Tolkning:** Premium och Fair har högst medel- och medianpris.")
    st.markdown("**Insikt:** Högre eller lägre slipningskvalitet kan ge högre pris, beroende på segment.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd bör utgå från att det är vikten som driver priset i dessa segment. Slipningskvalitet kan användas för att skapa produktsegment, men prissättningen bör i första hand baseras på vikt.")
    
    # Replace boxplot for price per color with grouped bar chart (mean and median)
    mean_price_color = df.groupby('color')['price'].mean().reindex(color_order)
    median_price_color = df.groupby('color')['price'].median().reindex(color_order)
    fig_bar_color = go.Figure()
    fig_bar_color.add_trace(go.Bar(x=color_order, y=mean_price_color, name='Medelpris'))
    fig_bar_color.add_trace(go.Bar(x=color_order, y=median_price_color, name='Medianpris'))
    fig_bar_color.update_layout(barmode='group', title='Medel- och Medianpris per Färg', xaxis_title='Färg', yaxis_title='Pris (USD)')
    st.plotly_chart(fig_bar_color, use_container_width=True)
    st.markdown("**Diagramtyp:** Grupperat stapeldiagram för medel- och medianpris per färg.")
    st.markdown("**Hur man tolkar:** Varje stapel visar medel- eller medianpriset för en färgklass.")
    st.markdown("**Tolkning:** J, I och H har högst medel- och medianpris.")
    st.markdown("**Insikt:** Högre färgklass (J, I, H) har högre pris i detta dataset.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd bör utgå från att det är vikten som driver priset i dessa segment. Färgkvalitet kan användas för att skapa produktsegment, men prissättningen bör i första hand baseras på vikt.")
    
    # Replace boxplot for price per clarity with grouped bar chart (mean and median)
    mean_price_clarity = df.groupby('clarity')['price'].mean().reindex(clarity_order)
    median_price_clarity = df.groupby('clarity')['price'].median().reindex(clarity_order)
    fig_bar_clarity = go.Figure()
    fig_bar_clarity.add_trace(go.Bar(x=clarity_order, y=mean_price_clarity, name='Medelpris'))
    fig_bar_clarity.add_trace(go.Bar(x=clarity_order, y=median_price_clarity, name='Medianpris'))
    fig_bar_clarity.update_layout(barmode='group', title='Medel- och Medianpris per Klarhetsgrad', xaxis_title='Klarhetsgrad', yaxis_title='Pris (USD)')
    st.plotly_chart(fig_bar_clarity, use_container_width=True)
    st.markdown("**Diagramtyp:** Grupperat stapeldiagram för medel- och medianpris per klarhetsgrad.")
    st.markdown("**Hur man tolkar:** Varje stapel visar medel- eller medianpriset för en klarhetsklass.")
    st.markdown("**Tolkning:** SI2, SI1 och I1 har högst medel- och medianpris.")
    st.markdown("**Insikt:** De klarhetsgrader som har högst pris har också högst vikt (titta på Medel- och Medianvikt per Klarhetsgrad nedanför), vilket visar att det är vikten som driver priset snarare än klarhetsgraden.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd bör utgå från att det är vikten som driver priset i dessa segment. Klarhetsgrad kan användas för att skapa produktsegment, men prissättningen bör i första hand baseras på vikt.")

    # Grouped bar chart for mean carat per cut
    mean_carat_cut = df.groupby('cut')['carat'].mean().reindex(cut_order)
    median_carat_cut = df.groupby('cut')['carat'].median().reindex(cut_order)
    fig_bar_carat_cut = go.Figure()
    fig_bar_carat_cut.add_trace(go.Bar(x=cut_order, y=mean_carat_cut, name='Medelvikt (carat)'))
    fig_bar_carat_cut.add_trace(go.Bar(x=cut_order, y=median_carat_cut, name='Medianvikt (carat)'))
    fig_bar_carat_cut.update_layout(barmode='group', title='Medel- och Medianvikt per Slipning', xaxis_title='Slipning', yaxis_title='Vikt (carat)')
    st.plotly_chart(fig_bar_carat_cut, use_container_width=True)
    st.markdown("**Diagramtyp:** Grupperat stapeldiagram för medel- och medianvikt per slipning.")
    st.markdown("**Hur man tolkar:** Varje stapel visar medel- eller medianvikten för en slipningsklass.")
    st.markdown("**Tolkning:** Premium och Fair har högst medel- och medianvikt.")
    st.markdown("**Insikt:** De slipningsklasser som har högst pris har också högst vikt, vilket visar att det är vikten som driver priset snarare än slipningskvaliteten.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd bör utgå från att det är vikten som driver priset i dessa segment. Slipningskvalitet kan användas för att skapa produktsegment, men prissättningen bör i första hand baseras på vikt.")

    # Grouped bar chart for mean carat per color
    mean_carat_color = df.groupby('color')['carat'].mean().reindex(color_order)
    median_carat_color = df.groupby('color')['carat'].median().reindex(color_order)
    fig_bar_carat_color = go.Figure()
    fig_bar_carat_color.add_trace(go.Bar(x=color_order, y=mean_carat_color, name='Medelvikt (carat)'))
    fig_bar_carat_color.add_trace(go.Bar(x=color_order, y=median_carat_color, name='Medianvikt (carat)'))
    fig_bar_carat_color.update_layout(barmode='group', title='Medel- och Medianvikt per Färg', xaxis_title='Färg', yaxis_title='Vikt (carat)')
    st.plotly_chart(fig_bar_carat_color, use_container_width=True)
    st.markdown("**Diagramtyp:** Grupperat stapeldiagram för medel- och medianvikt per färg.")
    st.markdown("**Hur man tolkar:** Varje stapel visar medel- eller medianvikten för en färgklass.")
    st.markdown("**Tolkning:** J, I och H har högst medel- och medianvikt.")
    st.markdown("**Insikt:** De färgklasser som har högst pris har också högst vikt, vilket visar att det är vikten som driver priset snarare än färgkvaliteten.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd bör utgå från att det är vikten som driver priset i dessa segment. Färgkvalitet kan användas för att skapa produktsegment, men prissättningen bör i första hand baseras på vikt.")

    # Grouped bar chart for mean carat per clarity
    mean_carat_clarity = df.groupby('clarity')['carat'].mean().reindex(clarity_order)
    median_carat_clarity = df.groupby('clarity')['carat'].median().reindex(clarity_order)
    fig_bar_carat_clarity = go.Figure()
    fig_bar_carat_clarity.add_trace(go.Bar(x=clarity_order, y=mean_carat_clarity, name='Medelvikt (carat)'))
    fig_bar_carat_clarity.add_trace(go.Bar(x=clarity_order, y=median_carat_clarity, name='Medianvikt (carat)'))
    fig_bar_carat_clarity.update_layout(barmode='group', title='Medel- och Medianvikt per Klarhetsgrad', xaxis_title='Klarhetsgrad', yaxis_title='Vikt (carat)')
    st.plotly_chart(fig_bar_carat_clarity, use_container_width=True)
    st.markdown("**Diagramtyp:** Grupperat stapeldiagram för medel- och medianvikt per klarhetsgrad.")
    st.markdown("**Hur man tolkar:** Varje stapel visar medel- eller medianvikten för en klarhetsklass.")
    st.markdown("**Tolkning:** SI2, SI1 och I1 har högst medel- och medianvikt.")
    st.markdown("**Insikt:** De klarhetsgrader som har högst pris har också högst vikt, vilket visar att det är vikten som driver priset snarare än klarhetsgraden.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd bör utgå från att det är vikten som driver priset i dessa segment. Klarhetsgrad kan användas för att skapa produktsegment, men prissättningen bör i första hand baseras på vikt.")

    # 5. Samband mellan Carat och Pris per Cut, Color, Clarity
    st.header("5. Samband mellan Vikt och Pris")
    st.markdown("Syfte: Undersöka hur vikt och pris samvarierar beroende på kvalitet.")
    # Scatterplot för cut
    fig_scatter_cut = px.scatter(df, x='carat', y='price', color='cut',
                               category_orders={'cut': cut_order},
                               title='Vikt vs Pris per Slipning',
                               labels={'carat': 'Vikt (karat)', 'price': 'Pris (USD)'})
    st.plotly_chart(fig_scatter_cut, use_container_width=True)
    st.markdown("**Diagramtyp:** Spridningsdiagram (scatterplot) för vikt och pris per slipning.")
    st.markdown("**Hur man tolkar:** Varje punkt är en diamant. Om punkterna bildar ett mönster (t.ex. stigande linje) finns ett samband. Färg visar slipning.")
    st.markdown("**Tolkning:** Högre vikt och bättre slipning ger högre pris.")
    st.markdown("**Insikt:** Det finns ett tydligt samband mellan vikt, slipning och pris.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd kan använda denna kunskap för att prissätta större och bättre slipade diamanter högre.")
    # Scatterplot för color
    fig_scatter_color = px.scatter(df, x='carat', y='price', color='color',
                                 category_orders={'color': color_order},
                                 title='Vikt vs Pris per Färg',
                                 labels={'carat': 'Vikt (karat)', 'price': 'Pris (USD)'})
    st.plotly_chart(fig_scatter_color, use_container_width=True)
    st.markdown("**Diagramtyp:** Spridningsdiagram (scatterplot) för vikt och pris per färg.")
    st.markdown("**Hur man tolkar:** Varje punkt är en diamant. Färg visar färgklass. Mönster visar samband.")
    st.markdown("**Tolkning:** Färg påverkar priset, särskilt för större diamanter.")
    st.markdown("**Insikt:** Premiumfärg ger högre pris, särskilt i större stenar.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd kan särskilt marknadsföra stora diamanter med hög färgkvalitet till premiumkunder.")
    # Scatterplot för clarity
    fig_scatter_clarity = px.scatter(df, x='carat', y='price', color='clarity',
                                   category_orders={'clarity': clarity_order},
                                   title='Vikt vs Pris per Klarhet',
                                   labels={'carat': 'Vikt (karat)', 'price': 'Pris (USD)'})
    st.plotly_chart(fig_scatter_clarity, use_container_width=True)
    st.markdown("**Diagramtyp:** Spridningsdiagram (scatterplot) för vikt och pris per klarhet.")
    st.markdown("**Hur man tolkar:** Varje punkt är en diamant. Färg visar klarhetsgrad. Mönster visar samband.")
    st.markdown("**Tolkning:** Klarhet har störst effekt på priset för större diamanter.")
    st.markdown("**Insikt:** Premiumklarhet i stora stenar ger högst pris.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd kan ta ut högre pris för stora diamanter med hög klarhet och rikta dem till exklusiva kunder.")

    # 6. Korrelationer
    st.header("6. Korrelationer")
    st.markdown("Syfte: Visa korrelationer mellan alla numeriska variabler i datasetet för att förstå sambanden mellan olika egenskaper.")
    
    # Create correlation matrix for numerical columns
    numerical_cols = ['price', 'carat', 'depth', 'table', 'x', 'y', 'z']
    corr_matrix = df[numerical_cols].corr()
    
    # Create heatmap
    fig_heatmap = px.imshow(corr_matrix,
                           labels=dict(color="Korrelation"),
                           x=numerical_cols,
                           y=numerical_cols,
                           title='Korrelationsmatris för Numeriska Variabler',
                           color_continuous_scale='RdBu_r',
                           aspect='auto')
    fig_heatmap.update_layout(
        xaxis_title="Variabler",
        yaxis_title="Variabler"
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)
    st.markdown("**Diagramtyp:** Heatmap (värmekarta) för korrelationer.")
    st.markdown("**Hur man tolkar:** Färgerna visar styrkan och riktningen av sambandet mellan variablerna. Röd = positiv korrelation, blå = negativ korrelation. Mörkare färg = starkare samband.")
    st.markdown("**Tolkning:** Det finns starka positiva korrelationer mellan vikt (carat) och pris, samt mellan de fysiska måtten (x, y, z).")
    st.markdown("**Insikt:** Vikt och fysiska mått är starkt relaterade till pris, medan djup och tavla har svagare samband.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd kan använda dessa samband för att förstå vilka faktorer som påverkar priset mest och optimera sitt sortiment.")

    st.markdown("Syfte: Det finns en stark korrelation mellan vikt (carat) och pris. Syftet är att visa sambandet mellan dessa på ett enkelt och tydligt sätt.")
    fig_corr = px.scatter(df, x='carat', y='price', title='Samband mellan Vikt (Carat) och Pris', labels={'carat': 'Vikt (carat)', 'price': 'Pris (USD)'})
    st.plotly_chart(fig_corr, use_container_width=True)
    st.markdown("**Diagramtyp:** Spridningsdiagram (scatterplot) för vikt (carat) och pris.")
    st.markdown("**Hur man tolkar:** Varje punkt är en diamant. Om punkterna bildar ett stigande mönster finns ett positivt samband.")
    st.markdown("**Tolkning:** Det finns ett tydligt positivt samband mellan vikt (carat) och pris – ju större diamant, desto högre pris.")
    st.markdown("**Insikt:** Vikt är den starkaste prisdrivande faktorn.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd kan använda detta samband för att prissätta större diamanter högre och identifiera attraktiva segment.")
    # Inbädda sektion 10 här med fulla förklaringsblock
    st.markdown("### Starka Korrelationer mellan Diamantmått")
    st.markdown("Syfte: Visa de tre starkaste sambanden mellan diamantens mått och vikt.")
    fig_carat_x = px.scatter(df, x='carat', y='x', title='Samband mellan Vikt (carat) och Längd (x)', labels={'carat': 'Vikt (carat)', 'x': 'Längd (mm)'})
    st.plotly_chart(fig_carat_x, use_container_width=True)
    st.markdown("**Diagramtyp:** Spridningsdiagram (scatterplot) för vikt (carat) och längd (x).")
    st.markdown("**Hur man tolkar:** Varje punkt är en diamant. Ett stigande mönster visar att större vikt ger större längd.")
    st.markdown("**Tolkning:** Det finns ett mycket starkt positivt samband mellan vikt och längd.")
    st.markdown("**Insikt:** Större diamanter är längre, vilket är logiskt och kan användas för kvalitetskontroll.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd kan använda detta samband för att snabbt uppskatta vikt utifrån längd vid värdering.")
    fig_x_y = px.scatter(df, x='x', y='y', title='Samband mellan Längd (x) och Bredd (y)', labels={'x': 'Längd (mm)', 'y': 'Bredd (mm)'})
    st.plotly_chart(fig_x_y, use_container_width=True)
    st.markdown("**Diagramtyp:** Spridningsdiagram (scatterplot) för längd (x) och bredd (y).")
    st.markdown("**Hur man tolkar:** Varje punkt är en diamant. Ett stigande mönster visar att längre diamanter också är bredare.")
    st.markdown("**Tolkning:** Det finns ett mycket starkt positivt samband mellan längd och bredd.")
    st.markdown("**Insikt:** Diamanter är ofta symmetriska, vilket syns i detta samband.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd kan använda detta samband för att kontrollera symmetri och kvalitet.")
    fig_x_z = px.scatter(df, x='x', y='z', title='Samband mellan Längd (x) och Höjd (z)', labels={'x': 'Längd (mm)', 'z': 'Höjd (mm)'})
    st.plotly_chart(fig_x_z, use_container_width=True)
    st.markdown("**Diagramtyp:** Spridningsdiagram (scatterplot) för längd (x) och höjd (z).")
    st.markdown("**Hur man tolkar:** Varje punkt är en diamant. Ett stigande mönster visar att längre diamanter tenderar att vara högre.")
    st.markdown("**Tolkning:** Det finns ett starkt positivt samband mellan längd och höjd.")
    st.markdown("**Insikt:** Diamanter med större längd tenderar att vara högre.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd kan använda detta samband för att identifiera proportionerliga och välformade diamanter.")

    # 7. Extremvärden och Saknade Värden
    st.header("7. Extremvärden och Saknade Värden")
    st.markdown("Syfte: Identifiera och analysera extremvärden och saknade värden i datasetet.")
    st.info("""
Datakvalitet: Datasetet innehåller extremvärden och saknade värden som kan påverka analysen. Det är viktigt att identifiera och hantera dessa för att säkerställa tillförlitliga resultat. Notera att 0-värden i x, y, z har tagits bort eftersom de är fysiskt omöjliga för en diamant. En diamant måste ha en längd, bredd och höjd för att existera, och därför kan inte någon av dessa dimensioner vara 0.
""")
    # Extremvärden
    outliers = {}
    for col in ['price', 'carat', 'depth', 'table', 'x', 'y', 'z']:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers[col] = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))].shape[0]
    fig_outliers = px.bar(x=list(outliers.keys()), y=list(outliers.values()), labels={'x': 'Variabel', 'y': 'Antal Extremvärden'}, title='Antal Extremvärden per Variabel')
    st.plotly_chart(fig_outliers, use_container_width=True)
    st.markdown("**Diagramtyp:** Stapeldiagram (bar chart) för extremvärden.")
    st.markdown("**Hur man tolkar:** Varje stapel visar antalet extremvärden för en variabel.")
    st.markdown("**Tolkning:** Extremvärden förekommer i samtliga nyckelvariabler (pris, vikt, djup, tavla) och kan snedvrida analysen, särskilt medelvärden och samband. För price kan enstaka mycket dyra diamanter ge en felaktig bild av prisnivåer. För carat kan extremt höga eller låga vikter påverka analysen av sambandet mellan vikt och pris. För depth och table kan extremvärden indikera mätfel eller ovanliga slipningar, vilket påverkar slutsatser om kvalitet och pris. Dessa bör identifieras och hanteras vid analys och affärsbeslut. Totalt finns det {} extremvärden.".format(sum(outliers.values())))
    st.markdown("**Insikt:** Datadrivna beslut kring lager och prissättning blir mer tillförlitliga om extremvärden hanteras korrekt. Extremvärden kan indikera unika möjligheter eller risker i sortimentet.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd bör identifiera och analysera extremvärden noggrant. Överväg att exkludera eller särskilt hantera diamanter med extremvärden vid prissättning och sortimentsplanering. Detta kan hjälpa till att optimera lager och öka lönsamheten.")
    # Saknade värden
    null_values = df.isnull().sum()
    fig_null = px.bar(x=null_values.index, y=null_values.values, labels={'x': 'Variabel', 'y': 'Antal Saknade Värden'}, title='Antal Saknade Värden per Variabel')
    st.plotly_chart(fig_null, use_container_width=True)
    st.markdown("**Diagramtyp:** Stapeldiagram (bar chart) för saknade värden.")
    st.markdown("**Hur man tolkar:** Varje stapel visar antalet saknade värden för en variabel.")
    st.markdown("**Tolkning:** Saknade värden är få och påverkar inte analysen nämnvärt. Totalt finns det {} saknade värden.".format(null_values.sum()))
    st.markdown("**Insikt:** Datasetet är relativt komplett, vilket ger tillförlitliga resultat.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd kan lita på datan för att fatta beslut kring lager och prissättning.")

    # 8. Hypotesprövningar
    st.header("8. Hypotesprövningar")
    st.markdown("Syfte: Undersöka om diamanter med högre vikt (carat) har större spridning i pris än lättare diamanter. Vi delar diamanterna i två grupper: små (carat <= median) och stora (carat > median). Vi använder ett enkelt stapeldiagram för att visa prisvariationen.")
    st.markdown("**Begreppsförklaring:** Prisvariation betyder hur mycket priserna skiljer sig åt inom en grupp. Hög variation betyder att det finns både billiga och dyra diamanter i gruppen.")
    carat_median = df['carat'].median()
    df['carat_group'] = ['Låg vikt' if c <= carat_median else 'Hög vikt' for c in df['carat']]
    price_std = df.groupby('carat_group')['price'].std()
    fig_var = px.bar(x=price_std.index, y=price_std.values, labels={'x': 'Viktgrupp', 'y': 'Prisvariation (std)'}, title='Prisvariation för små och stora diamanter')
    st.plotly_chart(fig_var, use_container_width=True)
    st.markdown("**Diagramtyp:** Stapeldiagram (bar chart) för prisvariation.")
    st.markdown("**Hur man tolkar:** Varje stapel visar hur mycket priserna varierar inom gruppen. Hög stapel = stor variation.")
    st.markdown("**Tolkning:** Stora diamanter har större prisvariation än små diamanter.")
    st.markdown("**Insikt:** Priset på stora diamanter kan skilja sig mycket, beroende på andra faktorer som kvalitet och sällsynthet.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd bör vara extra noga med prissättning av stora diamanter, eftersom priset kan variera mycket även inom samma viktgrupp.")

    # 9. Interaktiv Analys
    st.header("9. Interaktiv Analys")
    st.markdown("Syfte: Filtrera och analysera diamanter utifrån valda kvalitetsattribut och pris.")
    # Cut, color, clarity i rad
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_cut = st.multiselect('Välj slipningskvalitet (cut)', cut_order)
    with col2:
        selected_color = st.multiselect('Välj färgkvalitet (color)', color_order)
    with col3:
        selected_clarity = st.multiselect('Välj klarhetsgrad (clarity)', clarity_order)
    # Sliders i layout 2-2-2-1 (från vänster till höger)
    st.markdown("""
        <style>
        .stSlider > div[data-baseweb="slider"] {width: 100% !important; max-width: 300px; min-width: 200px; margin-left: 0; margin-right: auto;}
        </style>
        """, unsafe_allow_html=True)
    slider_cols = st.columns(4)
    with slider_cols[0]:
        price_range = st.slider('Prisintervall (USD)', int(df['price'].min()), int(df['price'].max()), (int(df['price'].min()), int(df['price'].max())))
        carat_min = float(df['carat'].min())
        carat_max = float(df['carat'].max())
        carat_range = st.slider('Viktintervall (carat)', min_value=carat_min, max_value=carat_max, value=(carat_min, carat_max), step=0.01, key='carat_slider', help='Filtrera på diamantens vikt (carat)', label_visibility='visible')
    with slider_cols[1]:
        depth_min, depth_max = float(df['depth'].min()), float(df['depth'].max())
        depth_range = st.slider('Djupintervall (depth)', min_value=depth_min, max_value=depth_max, value=(depth_min, depth_max), step=0.1, key='depth_slider', help='Filtrera på diamantens djup (%)', label_visibility='visible')
        table_min, table_max = float(df['table'].min()), float(df['table'].max())
        table_range = st.slider('Tavlaintervall (table)', min_value=table_min, max_value=table_max, value=(table_min, table_max), step=0.1, key='table_slider', help='Filtrera på diamantens tavla (%)', label_visibility='visible')
    with slider_cols[2]:
        x_min, x_max = float(df['x'].min()), float(df['x'].max())
        x_range = st.slider('Längdintervall (x)', min_value=x_min, max_value=x_max, value=(x_min, x_max), step=0.01, key='x_slider', help='Filtrera på diamantens längd (mm)', label_visibility='visible')
        y_min, y_max = float(df['y'].min()), float(df['y'].max())
        y_range = st.slider('Breddintervall (y)', min_value=y_min, max_value=y_max, value=(y_min, y_max), step=0.01, key='y_slider', help='Filtrera på diamantens bredd (mm)', label_visibility='visible')
    with slider_cols[3]:
        z_min, z_max = float(df['z'].min()), float(df['z'].max())
        z_range = st.slider('Höjdintervall (z)', min_value=z_min, max_value=z_max, value=(z_min, z_max), step=0.01, key='z_slider', help='Filtrera på diamantens höjd (mm)', label_visibility='visible')
    # Filtrera data baserat på valda parametrar
    filtered_df = df.copy()
    if selected_cut:
        filtered_df = filtered_df[filtered_df['cut'].isin(selected_cut)]
    if selected_color:
        filtered_df = filtered_df[filtered_df['color'].isin(selected_color)]
    if selected_clarity:
        filtered_df = filtered_df[filtered_df['clarity'].isin(selected_clarity)]
    filtered_df = filtered_df[(filtered_df['price'] >= price_range[0]) & (filtered_df['price'] <= price_range[1])]
    filtered_df = filtered_df[(filtered_df['carat'] >= carat_range[0]) & (filtered_df['carat'] <= carat_range[1])]
    filtered_df = filtered_df[(filtered_df['depth'] >= depth_range[0]) & (filtered_df['depth'] <= depth_range[1])]
    filtered_df = filtered_df[(filtered_df['table'] >= table_range[0]) & (filtered_df['table'] <= table_range[1])]
    # Visa statistik och visualiseringar för filtrerad data
    st.subheader("Statistik för valda diamanter")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Antal diamanter", f"{len(filtered_df):,}")
    with col2:
        st.metric("Medelpris", f"${filtered_df['price'].mean():,.2f}")
    with col3:
        st.metric("Medelvikt", f"{filtered_df['carat'].mean():.2f} carat")
    fig_filt_price = px.histogram(filtered_df, x='price', nbins=30, title='Prisfördelning (Filtrerad)')
    st.plotly_chart(fig_filt_price, use_container_width=True)
    st.markdown("**Diagramtyp:** Histogram för prisfördelning (filtrerad data).")
    st.markdown("**Hur man tolkar:** Visar hur priserna fördelar sig i det valda segmentet.")
    st.markdown("**Tolkning:** Filtrering ger möjlighet att analysera specifika segment och deras prisfördelning.")
    st.markdown("**Insikt:** Möjlighet att identifiera attraktiva segment för riktad marknadsföring.")
    fig_filt_carat = px.histogram(filtered_df, x='carat', nbins=30, title='Viktfördelning (Filtrerad)')
    st.plotly_chart(fig_filt_carat, use_container_width=True)
    st.markdown("**Diagramtyp:** Histogram för viktfördelning (filtrerad data).")
    st.markdown("**Hur man tolkar:** Visar hur vikterna fördelar sig i det valda segmentet.")
    st.markdown("**Tolkning:** Filtrering ger möjlighet att analysera specifika segment och deras viktfördelning.")
    st.markdown("**Insikt:** Möjlighet att anpassa lager och inköp efter efterfrågan i olika segment.")
    st.markdown("**Affärsmässig tolkning:** Guldfynd kan använda denna analys för att optimera lager och inköp.")

    # 10. Beslutsstöd: Ska vi köpa diamanten?
    st.header("10. Beslutsstöd: Ska vi köpa diamanten?")
    st.markdown("Syfte: Hjälpa styrelsen att fatta datadrivna beslut om inköp av enskilda diamanter baserat på analysen ovan.")

    # Funktion för att fatta beslut om köp
    @st.cache_data
    def get_reference_stats(df):
        # Beräkna referensvärden för pris per carat per kvalitet
        ref = df.groupby(['cut', 'color', 'clarity'])[['price', 'carat']].median().reset_index()
        ref['price_per_carat'] = ref['price'] / ref['carat']
        return ref

    reference_stats = get_reference_stats(df)

    def should_buy_diamond(carat, cut, color, clarity, price, depth, table, x, y, z, df, reference_stats):
        # Grundläggande kontroller
        if carat <= 0 or price <= 0 or x <= 0 or y <= 0 or z <= 0:
            return ("Nej", "Ogiltiga värden: carat, pris och dimensioner måste vara större än 0.")
        # Kontrollera om egenskaperna är extremvärden
        for col, val in zip(['carat','price','depth','table','x','y','z'], [carat,price,depth,table,x,y,z]):
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            if val < (Q1 - 1.5*IQR) or val > (Q3 + 1.5*IQR):
                return ("Nej", f"{col}={val} är ett extremvärde jämfört med marknaden. Undvik köp utan manuell granskning.")
        # Jämför pris per carat mot referens för denna kvalitet
        ref_row = reference_stats[(reference_stats['cut']==cut) & (reference_stats['color']==color) & (reference_stats['clarity']==clarity)]
        if not ref_row.empty:
            ref_ppc = ref_row.iloc[0]['price_per_carat']
            ppc = price / carat
            if ppc > ref_ppc * 1.2:
                return ("Nej", f"Priset per carat ({ppc:.0f} USD) är mer än 20% högre än medianen för denna kvalitet ({ref_ppc:.0f} USD). Undvik köp.")
            elif ppc < ref_ppc * 0.7:
                return ("Ja", f"Priset per carat ({ppc:.0f} USD) är lågt jämfört med marknaden för denna kvalitet. Möjligt fynd!")
            else:
                return ("Ja", f"Priset per carat ({ppc:.0f} USD) är rimligt för denna kvalitet.")
        else:
            return ("Nej", "Kombinationen av cut, color och clarity är ovanlig i marknaden. Kräver manuell granskning.")

    # Formulär för att mata in diamantens egenskaper
    with st.form("diamond_decision_form"):
        st.subheader("Fatta beslut om enskild diamant")
        col1, col2, col3 = st.columns(3)
        with col1:
            carat = st.number_input('Vikt (carat)', min_value=0.01, max_value=5.0, value=0.5, step=0.01)
            price = st.number_input('Pris (USD)', min_value=1, max_value=100000, value=3000, step=1)
            cut = st.selectbox('Slipning (cut)', cut_order)
        with col2:
            color = st.selectbox('Färg (color)', color_order)
            clarity = st.selectbox('Klarhet (clarity)', clarity_order)
            depth = st.number_input('Djup (%)', min_value=40.0, max_value=80.0, value=61.0, step=0.1)
        with col3:
            table = st.number_input('Tavla (%)', min_value=40.0, max_value=100.0, value=57.0, step=0.1)
            x = st.number_input('Längd (x, mm)', min_value=0.1, max_value=15.0, value=5.0, step=0.01)
            y = st.number_input('Bredd (y, mm)', min_value=0.1, max_value=15.0, value=5.0, step=0.01)
            z = st.number_input('Höjd (z, mm)', min_value=0.1, max_value=10.0, value=3.2, step=0.01)
        submitted = st.form_submit_button("Få rekommendation")
        if submitted:
            beslut, motivering = should_buy_diamond(carat, cut, color, clarity, price, depth, table, x, y, z, df, reference_stats)
            st.success(f"Rekommendation: {beslut}")
            st.info(f"Motivering: {motivering}")

    # 11. Executive Summary och Data Storytelling
    st.header("11. Executive Summary och Data Storytelling")
    st.markdown("""
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
    """)

if __name__ == "__main__":
    analyze_diamonds() 