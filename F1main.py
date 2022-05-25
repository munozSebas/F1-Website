import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import requests
import plotly.graph_objects as go
from altair.examples.pyramid import df

st.title ("F1 RACING")
imgT = Image.open("F1.svg.png")
st.image(imgT)

#---------------------------------SIDEBAR--------------------
add_selectbox = st.sidebar.selectbox(
"MORE ABOUT F1",
("MAIN", "ABOUT", "WHY F1","SEASON OVERVIEW", "BECOME A DRIVER" ,"CREDITS"))

if add_selectbox == "ABOUT":
    st.info("Click the link to learn more about F1")
    st.write("ABOUT F1: https://corp.formula1.com/about-f1/ ")
    imgA = Image.open("f1OTHERPIC.jpg")
    st.image(imgA)

elif add_selectbox == "WHY F1":
    st.write("F1 is a fascinating sport that millions across the world come togther to watch drivers who represent their country compete to win"
             " a trophy. A fast exilirating sport that millions of new watchers can enjoy.")
    img = Image.open("f1GROUP.jpg")
    st.image(img)

    st.write("So we chose this project to demonstrate to new watchers about F1's stats, the current drivers and show some of F1's famous stadiums."
             "“In racing there are always things you can learn, every single day. There is always space for improvement, and I think that applies to everything in life.” –  Lewis Hamilton")
    img2 = Image.open("f1CAR.jpeg")
    st.image(img2)

elif add_selectbox == "SEASON OVERVIEW":

    st.write("Here we will discuss the F1 current season so far, by showing you charts relating to the point each team has earned. \n And who is leading team and driver"
             " .")
    st.write("F1 consist of two drivers where each take a turn and try to make as much as possible \n "
             "1st being the most points you can obtain (25) and you can obtain an extra point if you complete the fastest lap. 10th being the least amount of points you can obtain (1): ")

    # ----------------------------------------top team api info----------------------------------------------------

    teamUrl = "https://api-formula-1.p.rapidapi.com/rankings/teams"

    querystring = {"season": "2022"}

    headers = {
        "X-RapidAPI-Host": "api-formula-1.p.rapidapi.com",
        "X-RapidAPI-Key": "bf6dc6b71cmsh024507990a594eep1f96c2jsn8b27d8111492"
    }

    teamResponse = requests.request("GET", teamUrl, headers=headers, params=querystring)
    teamResponse_data = teamResponse.json()
    # st.write(teamResponse_data)
    topTeamName = teamResponse_data["response"][0]["team"]["name"]
    topTeamLogo = teamResponse_data["response"][0]["team"]["logo"]
    topTeamPoints = teamResponse_data["response"][0]["points"]

    st.write("the current leading team is", topTeamName, "with", topTeamPoints, "points!")
    st.image("{0}".format(topTeamLogo))


    # ------------------------------------top driver api info--------------------------------------------------------------------------

    driverUrl = "https://api-formula-1.p.rapidapi.com/rankings/drivers"

    querystring = {"season": "2022"}

    headers = {
        "X-RapidAPI-Host": "api-formula-1.p.rapidapi.com",
        "X-RapidAPI-Key": "bf6dc6b71cmsh024507990a594eep1f96c2jsn8b27d8111492"
    }

    driverResponse = requests.request("GET", driverUrl, headers=headers, params=querystring)
    driverResponse_data = driverResponse.json()
    # st.write(driverResponse_data)
    topDriverName = driverResponse_data["response"][0]["driver"]["name"]
    topDriverImage = driverResponse_data["response"][0]["driver"]["image"]
    topDriverPoints = driverResponse_data["response"][0]["points"]
    topDriverTeam = driverResponse_data["response"][0]["team"]["name"]

    st.write("the current leading driver is", topDriverName, "with", topDriverPoints, "points!")
    st.image("{0}".format(topDriverImage))

    # ---------------------------------------drivers championship line chart------------------------------------------------------

    # initialize arrays for each drivers points
    hamPos = [0, 0, 0, 0, 0]
    rusPos = [0, 0, 0, 0, 0]
    verPos = [0, 0, 0, 0, 0]
    perPos = [0, 0, 0, 0, 0]
    lecPos = [0, 0, 0, 0, 0]
    saiPos = [0, 0, 0, 0, 0]
    norPos = [0, 0, 0, 0, 0]
    ricPos = [0, 0, 0, 0, 0]
    aloPos = [0, 0, 0, 0, 0]
    ocoPos = [0, 0, 0, 0, 0]
    gasPos = [0, 0, 0, 0, 0]
    tsuPos = [0, 0, 0, 0, 0]
    vetPos = [0, 0, 0, 0, 0]
    strPos = [0, 0, 0, 0, 0]
    albPos = [0, 0, 0, 0, 0]
    latPos = [0, 0, 0, 0, 0]
    botPos = [0, 0, 0, 0, 0]
    zhoPos = [0, 0, 0, 0, 0]
    magPos = [0, 0, 0, 0, 0]
    shuPos = [0, 0, 0, 0, 0]

    circuits = ["bahrain GP", "Saudi Arabian GP", "Australian GP", "Emilia Romagna GP", "Miami GP"]

    raceId = 0
    # for loop to go through each grand prix
    for i in range(0, 5):

        if i == 0:
            raceId = 1488
        elif i == 1:
            raceId = 1493
        elif i == 2:
            raceId = 1498
        elif i == 3:
            raceId = 1503
        elif i == 4:
            raceId = 1508

        race1Url = "https://api-formula-1.p.rapidapi.com/rankings/races"

        querystring = {"race": "{0}".format(raceId)}

        headers = {
            "X-RapidAPI-Host": "api-formula-1.p.rapidapi.com",
            "X-RapidAPI-Key": "bf6dc6b71cmsh024507990a594eep1f96c2jsn8b27d8111492"
        }

        race1Response = requests.request("GET", race1Url, headers=headers, params=querystring)
        race1Response_data = race1Response.json()
        # st.write(race1Response_data)
        # for loop to iterate through every driver and assign position for grand prix
        for entry in race1Response_data["response"]:
            if entry["driver"]["name"] == "Lewis Hamilton":
                hamPos[i] = entry["position"]
            elif entry["driver"]["name"] == "George Russell":
                rusPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Max Verstappen":
                verPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Sergio Perez":
                perPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Charles Leclerc":
                lecPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Carlos Sainz Jr":
                saiPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Lando Norris":
                norPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Daniel Ricciardo":
                ricPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Fernando Alonso":
                aloPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Esteban Ocon":
                ocoPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Pierre Gasly":
                gasPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Yuki Tsunoda":
                tsuPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Nico Hulkenberg":
                vetPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Nico Hulkenberg":
                vetPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Lance Stroll":
                strPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Valtteri Bottas":
                botPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Guanyu Zhou":
                zhoPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Alexander Albon":
                albPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Nicholas Latifi":
                latPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Kevin Magnussen":
                magPos[i] = entry["position"]
            elif entry["driver"]["name"] == "Mick Schumacher":
                shuPos[i] = entry["position"]


    # function to convert position to points
    def position_to_points(x):
        if x[0] == 1:
            x[0] = 25
        elif x[0] == 2:
            x[0] = 18
        elif x[0] == 3:
            x[0] = 15
        elif x[0] == 4:
            x[0] = 12
        elif x[0] == 5:
            x[0] = 10
        elif x[0] == 6:
            x[0] = 8
        elif x[0] == 7:
            x[0] = 6
        elif x[0] == 8:
            x[0] = 4
        elif x[0] == 9:
            x[0] = 2
        elif x[0] == 10:
            x[0] = 1
        else:
            x[0] = 0
        for i in range(1, 5):
            if x[i] == 1:
                x[i] = x[i - 1] + 25
            elif x[i] == 2:
                x[i] = x[i - 1] + 18
            elif x[i] == 3:
                x[i] = x[i - 1] + 15
            elif x[i] == 4:
                x[i] = x[i - 1] + 12
            elif x[i] == 5:
                x[i] = x[i - 1] + 10
            elif x[i] == 6:
                x[i] = x[i - 1] + 8
            elif x[i] == 7:
                x[i] = x[i - 1] + 6
            elif x[i] == 8:
                x[i] = x[i - 1] + 4
            elif x[i] == 9:
                x[i] = x[i - 1] + 2
            elif x[i] == 10:
                x[i] = x[i - 1] + 1
            else:
                x[i] = x[i - 1] + 0


    # convert position for each driver into points
    position_to_points(hamPos)
    position_to_points(rusPos)
    position_to_points(verPos)
    position_to_points(perPos)
    position_to_points(lecPos)
    position_to_points(saiPos)
    position_to_points(norPos)
    position_to_points(ricPos)
    position_to_points(aloPos)
    position_to_points(ocoPos)
    position_to_points(gasPos)
    position_to_points(tsuPos)
    position_to_points(vetPos)
    position_to_points(strPos)
    position_to_points(albPos)
    position_to_points(latPos)
    position_to_points(botPos)
    position_to_points(zhoPos)
    position_to_points(magPos)
    position_to_points(shuPos)

    driversFig = go.Figure()

    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=hamPos,
        name="Lewis Hamilton"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=rusPos,
        name="George Russell"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=verPos,
        name="Max Verstappen"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=perPos,
        name="Sergio Perez"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=lecPos,
        name="Charles Leclerc"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=saiPos,
        name="Carlos Sainz Jr"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=norPos,
        name="Lando Norris"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=ricPos,
        name="Daniel Ricciardo"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=aloPos,
        name="Fernando Alonso"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=ocoPos,
        name="Esteban Ocon"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=gasPos,
        name="Pierre Gasly"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=tsuPos,
        name="Yuki Tsunoda"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=vetPos,
        name="Sebastion Vettel"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=strPos,
        name="Lance Stroll"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=botPos,
        name="Valtteri Bottas"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=zhoPos,
        name="Guanyu Zhou"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=magPos,
        name="Kevin Magnussen"
    ))
    driversFig.add_trace(go.Scatter(
        x=circuits,
        y=shuPos,
        name="Mick Shumacher"
    ))


    driversFig.update_layout(

        title="drivers championship standing",
        xaxis_title="circuit",
        yaxis_title="points",
        legend_title="driver"
    )



    st.title('2022 Driver Standings')

    driverStandings = pd.read_csv('2022driverstandings1.csv')

    st.dataframe(driverStandings)

    st.info("Under driver you can click on each point to deselect them from the chart. \n So you can focus on the teams standing you wish to see.")
    st.plotly_chart(driversFig)
    st.info("note: lines will flatline after last race")

    # ------------------------------------Constructors championship standings-------------

    # initialize arrays for each drivers points
    mercedesPos = [0, 0, 0, 0, 0]
    redBullPos = [0, 0, 0, 0, 0]
    ferrariPos = [0, 0, 0, 0, 0]
    mclarenPos = [0, 0, 0, 0, 0]
    alpinePos = [0, 0, 0, 0, 0]
    alphaTauriPos = [0, 0, 0, 0, 0]
    astonMartinPos = [0, 0, 0, 0, 0]
    williamsPos = [0, 0, 0, 0, 0]
    alfaRomeoPos = [0, 0, 0, 0, 0]
    haasPos = [0, 0, 0, 0, 0]

    circuits = ["bahrain GP", "Saudi Arabian GP", "Australian GP", "Emilia Romagna GP", "Miami GP"]

    # convert points for each driver into team points
    mercedesPos = hamPos
    redBullPos = verPos
    ferrariPos = lecPos
    mclarenPos = norPos
    alpinePos = aloPos
    alphaTauriPos = gasPos
    astonMartinPos = vetPos
    williamsPos = albPos
    alfaRomeoPos = botPos
    haasPos = magPos

    for i in range(0, 5):
        mercedesPos[i] += rusPos[i]
        redBullPos[i] += perPos[i]
        ferrariPos[i] += saiPos[i]
        mclarenPos[i] += ricPos[i]
        alpinePos[i] += ocoPos[i]
        alphaTauriPos[i] += tsuPos[i]
        astonMartinPos[i] += strPos[i]
        williamsPos[i] += latPos[i]
        alfaRomeoPos[i] += zhoPos[i]
        haasPos[i] += shuPos[i]

    teamFig = go.Figure()

    teamFig.add_trace(go.Scatter(
        x=circuits,
        y=mercedesPos,
        name="Mercedes"
    ))
    teamFig.add_trace(go.Scatter(
        x=circuits,
        y=redBullPos,
        name="Red Bull Racing"
    ))
    teamFig.add_trace(go.Scatter(
        x=circuits,
        y=ferrariPos,
        name="Ferrari"
    ))
    teamFig.add_trace(go.Scatter(
        x=circuits,
        y=mclarenPos,
        name="Mclaren"
    ))
    teamFig.add_trace(go.Scatter(
        x=circuits,
        y=alphaTauriPos,
        name="Alpha Tauri"
    ))
    teamFig.add_trace(go.Scatter(
        x=circuits,
        y=alpinePos,
        name="Alpine"
    ))
    teamFig.add_trace(go.Scatter(
        x=circuits,
        y=astonMartinPos,
        name="Aston Martin"
    ))
    teamFig.add_trace(go.Scatter(
        x=circuits,
        y=williamsPos,
        name="Williams"
    ))
    teamFig.add_trace(go.Scatter(
        x=circuits,
        y=alfaRomeoPos,
        name="Alfa Romeo"
    ))
    teamFig.add_trace(go.Scatter(
        x=circuits,
        y=haasPos,
        name="Haas"
    ))

    teamFig.update_layout(
        title="Constructors championship standing",
        xaxis_title="circuit",
        yaxis_title="points",
        legend_title="Constructor"
    )

    st.plotly_chart(teamFig)
    st.info("note: lines will flatline after last race")








#---------------------- BECOME A DRIVER-------------------------
elif add_selectbox == "BECOME A DRIVER":
    st.write("So you want to become a F1 driver? ")
    st.write("Below there will be criterias that you need to enter to become an F1 driver")

    user_create = st.text_input("What is your name?")
    if user_create:
        st.write ("Hello", user_create )
        st.subheader("TEAM SELECTION")

        team_pick = st.radio ("WHICH TEAM WOULD YOU LIKE TO BE PART OF ?: ",
                              (' ', 'Alfa Romeo','Alpha Tauri','Alpine', 'Aston Martin','Ferrari', 'HAAS','McLaren','Mercedes', 'Red Bull', 'Williams'))
        if team_pick == 'Ferrari':
            st.write('Fast like the logo you got speed we want!')
            imgFR = Image.open("ferrariF1.png.crdownload")
            st.image(imgFR)

        elif team_pick == 'Mercedes':
            st.write('Luxorious vehicle you chose to ride with style, Great to have you on the team!')
            imgMB = Image.open("mercF1.png")
            st.image(imgMB)


        elif team_pick == 'Red Bull':
            st.write('Raging like the bull now you have the wings to soar through the competition')
            imgRB = Image.open("redbullF1.png")
            st.image(imgRB)

        elif team_pick == 'McLaren':
            st.write('Be one of a kind, Be sharp, You are now McLaren')
            imgMCL = Image.open("mcF1.png.crdownload")
            st.image(imgMCL)

        elif team_pick == 'Alpine':
            st.write('You climbed that tall mountain, now its time to go down it at a ferocius speed')
            imgAlp = Image.open("AlpF1.png")
            st.image(imgAlp)

        elif team_pick == 'Alpha Tauri':
            st.write('You are the Alpha of the track, now go out there and claim your Victory')
            imgALPH = Image.open("alphaF1.png")
            st.image(imgALPH)

        elif team_pick == 'Aston Martin':
            st.write('No one can Rival us, we are there when you least expect and will make that grand finale')
            imgAST = Image.open("AstonF1.png.crdownload")
            st.image(imgAST)

        elif team_pick == 'Alfa Romeo':
            st.write('Be the visconti serpent, strike when they least expect it and win.')
            imgAlf = Image.open("AlfaF1.png")
            st.image(imgAlf)

        elif team_pick == 'Williams':
            st.write('You have the WILL to overcome any obstacle, lets go out and leave them in the dust.')
            imgWILL = Image.open("WillF1.png")
            st.image(imgWILL)

        elif team_pick == 'HAAS':
            st.write('You will never be a HAAS been in our team, now lets HAVE that trophy')
            imgHAAS = Image.open("HAASF1.png.crdownload")
            st.image(imgHAAS)


        if team_pick: st.write('Insert a photo of yourself so we can add you to our ', team_pick, 'roster')


        uploaded_file = st.file_uploader("ENTER YOUR PHOTO AND THE CAR YOU WISH YOU DRIVE!", accept_multiple_files=True)
        st.warning("Please enter a JPG,JPEG,PNG file")
        for uploaded_file in uploaded_file:
            bytes_data = uploaded_file.read()
            st.image(uploaded_file)

            if uploaded_file:
                number = st.slider('Slide the cursor to pick your number!', 00,99, 0)
                if number:
                 st.balloons()
                 st.success("WELCOME")
                 st.write(user_create, ' you are now part of', team_pick, 'and your number is', number)
                 st.write ('NOW GO OUT THERE AND WIN A TROPHY FOR US AND MAKE HISTORY')


#-----------------------CREDITS-------------------
elif add_selectbox == "CREDITS":
    st.write("SEBASTIAN MUNOZ,SAMUEL HUEZO, ALEX GARCIA, DEXTER TOURNESY, GLEN SEDO, LUIS SANCHEZ")


#------------------MAIN PAGE-----------
    st.subheader("Your go to place to learn about F1 racing")

else:

    st.subheader("F1 Teams and their drivers")

    st.write("WOULD YOU LIKE TO SEE THE 2nd DRIVER ?")
    scndDriver = st.button('YES')
    if scndDriver:
        st.success("THE DRIVERS ARE BELOW")
    st.info("Click NO to take out the 2nd drivers")
    scndDriverNO = st.button('NO')

    st.subheader("Alfa Romeo")
    with st.expander("TO SEE ALFA ROMEO LOGO"):
        imagALFL = Image.open("AlfaF1.png")
        st.image(imagALFL)

    st.write("77.Valtteri Bottas")
    imagVAL = Image.open("f1VALT.jpg")
    st.image(imagVAL)


    if scndDriver:
     st.write("24.Guanyu Zhou")
     imagGUAN = Image.open ("f1GUAN.jpg")
     st.image(imagGUAN)

    st.subheader("Alpha Tauri")
    with st.expander("TO SEE ALPHA TAURI LOGO"):
        imagALPHL = Image.open("alphaF1.png")
        st.image(imagALPHL)
    st.write("10.Pierre Gasly")
    imagPIE = Image.open("f1PIERRE.jpg")
    st.image(imagPIE)

    if scndDriver:
        st.write("22.Yuki Tsunoda")
        imagYUKI = Image.open("f1YUKI.jpg")
        st.image(imagYUKI)

    st.subheader("Alpine")
    with st.expander("TO SEE ALPINE LOGO"):
        imagALPL = Image.open("AlpF1.png")
        st.image(imagALPL)
    st.write("14.Fernando Alonso")
    imagFERN = Image.open("f1FERN.jpg")
    st.image(imagFERN)

    if scndDriver:
        st.write("31.Esteban Ocon")
        imagESTE = Image.open("f1ESTEB.jpg")
        st.image(imagESTE)

    st.subheader("Aston Martin")
    with st.expander("TO SEE ASTON MARTIN LOGO"):
        imagASTL = Image.open("AstonF1.png.crdownload")
        st.image(imagASTL)

    st.write("5.Sebastian Vettel")
    imagSEBAS = Image.open("f1SEBAS.jpg")
    st.image(imagSEBAS)
    if scndDriver:
        st.write("18.Lance Stroll")
        imagLANCE = Image.open("f1LANCE.jpg")
        st.image(imagLANCE)

    st.subheader("Ferrari")
    with st.expander("TO SEE FERRARI LOGO"):
        imagFERRL = Image.open("ferrariF1.png.crdownload")
        st.image(imagFERRL)
    st.write("16.Charles Leclerc")
    imagCHARL = Image.open("f1CHARLES.jpg")
    st.image(imagCHARL)
    if scndDriver:
        st.write("55.Carlos Sainz Jr.")
        imagCARL = Image.open("f1CARLOS.webp")
        st.image(imagCARL)

    st.subheader("HAAS")
    with st.expander("TO SEE HAAS LOGO"):
        imagHAASL = Image.open("HAASF1.png.crdownload")
        st.image(imagHAASL)
    st.write("47.Mick Schumacher")
    imagMICK = Image.open("f1MICK.jpg")
    st.image(imagMICK)
    if scndDriver:
        st.write("20.Kevin Magnussen")
        imagKEVIN = Image.open("f1KEVIN.jpg")
        st.image(imagKEVIN)

    st.subheader("McLaren")
    with st.expander("TO SEE MCLAREN LOGO"):
        imagMCLL = Image.open("mcF1.png.crdownload")
        st.image(imagMCLL)
    st.write("3.Daniel Ricciardo")
    imagDANIEL = Image.open("f1DANIEL.jpg")
    st.image(imagDANIEL)
    if scndDriver:
        st.write("4.Lando Norris")
        imagLANDO = Image.open("f1LANDO.jpg")
        st.image(imagLANDO)

    st.subheader("Mercedes")
    with st.expander("TO SEE MERCEDES LOGO"):
        imagMERCL = Image.open("mercF1.png")
        st.image(imagMERCL)
    st.write("44.Lewis Hamilton")
    imagLEWIS = Image.open("f1Lewis.jpg")
    st.image(imagLEWIS)
    if scndDriver:
        st.write("63.George Russell")
        imagGEOR = Image.open("f1GEORGE.jpg")
        st.image(imagGEOR)

    st.subheader("RedBull")
    with st.expander("TO SEE REDBULL LOGO"):
        imagRBL = Image.open("redbullF1.png")
        st.image(imagRBL)
    st.write("33.Max Verstappen")
    imagMAX = Image.open("f1MAX.jpg")
    st.image(imagMAX)
    if scndDriver:
        st.write("11.Sergio Pérez")
        imagSERG = Image.open("f1SERG.jpg")
        st.image(imagSERG)

    st.subheader("Williams")
    with st.expander("TO SEE WILLIAMS LOGO"):
        imagWILLL = Image.open("WillF1.png")
        st.image(imagWILLL)
    st.write("23.Alex Albon")
    imagALEX = Image.open("f1ALEXAN.jpg")
    st.image(imagALEX)
    if scndDriver:
        st.write("6.Nicholas Latifi")
        imagNICH = Image.open("f1NICH.jpg")
        st.image(imagNICH)

#---------------------------- FAMOUS CIRCUITS-------------------------
    st.subheader("F1's Famous Circuits")

    option = st.selectbox("Select",options=["Fuji Speedway","Rockingham Motor Speedway", "Shanghai International Circuit", "Circuit De Monaco", "Autodromo Hermanos Rodriguez"])

    if option =="Fuji Speedway":
        st.info("This circuit is located at Japan Nakahinata, Oyama \n It rest on the foothills of Mount Fuji ")
        st.write("Fun fact: The Fuji Speedway is known for having one of the longest straights.")
        st.write("*A STRAIGHT IS JUST A STRAIGHT AWAY DOWN A TRACK")
        imagFS = Image.open("FJSPEED.jpg.crdownload")
        st.image(imagFS)
    if option =="Rockingham Motor Speedway":
        st.info("This circuit is located at Rockingham, Northamptonshire, England, United Kingdom")
        st.write ("Fun fact: Rockingham Motor Speedway is now a former motor speedway, but it still holds a dear place in the hearts of F1 fans. The racing of the F1 cars "
                  "can still be heard.")
        imagRH = Image.open("F1RH.jpg")
        st.image(imagRH)
    if option =="Shanghai International Circuit":
        st.info("This circuit is located at Shanghai, China in the Jiading District")
        st.write ("Fun fact: The track layout of the circuit was inspired by the Symbol 上. Meaning Shang")
        st.write("SHANG meaning above and ascend")
        imagSH = Image.open("F1SH.jpg")
        st.image(imagSH)
    if option == "Circuit De Monaco":
        st.info("This circuit is located in the streets of Monte Carlo (France) \n And on the edge of harbour Principality of Monaco ")
        st.write("Fun fact: Monaco will be hosting an race soon from May 26,2022 - May 29,2022. Get your tickets quick")
        imagMC = Image.open("F1MC.jpg")
        st.image(imagMC)
    if option == "Autodromo Hermanos Rodriguez":
        st.info("This circuit is located at Mexico, in Magdalena Mixhuca Mexico City.")
        st.write("Fun fact: The circuit is named after the Rodriguez brothers who have sadly past away. \n Hermano = Brother")
        imagMC = Image.open("F1AD.jpg")
        st.image(imagMC)

#--------------------MAP-------------------------
    st.subheader("MAP LOCATION OF CIRCUITS")
    st.info("CHECK SPEEDWAYS TO SEE WHERE THE CIRCUITS ARE LOCATED IN THE WORLD")
    speed_ways = st.checkbox("SPEEDWAYS")
    if speed_ways:
        st.write("FAMOUS F1 CIRCUITS")
        map_data = pd.DataFrame(
            np.array([
                [35.3728, 138.9288],  #fuji
                [43.733334, 7.416667],  #Monaco
                [ 52.508953, -0.680215], #Rockingham
                [34.9763, 79.6131],  #shanghai
                [19.4032, -99.0893]]), #autodromo
            columns=['lat','lon'])
        st.map(map_data)
        st.info("To ZOOM IN scroll wheel DOWN"
                "  \n To ZOOM OUT scroll wheel UP")






