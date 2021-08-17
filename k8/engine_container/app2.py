### Import nessicary modules
from flask import Flask,request, jsonify         #imports the core functionalities for running the APIs
import os
import logging
from sqlalchemy import create_engine
import pandas as pd
import synthSportPlayer

#This initialises the app. Do not change the __name__
app = Flask(__name__)                            

#This sets up the route to activate the following function and the method that it will recieve
@app.route('/progress', methods=['PUT'])          
def progress():
    if ls:                                                      #If the live season exists
        try:                                                    #try to
            ls.playSeason()                                     #move the season on a step
            print('season ticked')
            if ls.currentTournComplete:                         #if the current tournament is complete
                tab=ls.playerSum.iloc[:,[0,-1]].copy()
                tab['week']=tab.columns[-1]
                tab.rename(columns={tab.columns[-2]: "points"},inplace=True)
                tab.to_sql("RANKING_DATA",engine,index=False,if_exists='append') #update the table rankings
                
            return jsonify()
        except:
            print("Live season error")
    else:                                                       #if the live season does not exist
        print ('Load the live season first')
        return ('No season here to use')                         #return the information

@app.route('/ready',methods=['GET'])
def ready():
    return jsonify()

    

#when the app first launches it will run the "__main__" body first to set anything up.
if __name__ == '__main__':                           
    # Get environment variables
    # These will be inserted from pod def file!

    print('Establishing ENV variables')
    
    USER = os.getenv('MYSQL_USER')          #source from srt, should be 'postgres'
    PASSWORD = os.getenv('MYSQL_PASSWORD')  #source from srt
    DB = os.getenv('MYSQL_DATABASE')        #source from cfmp, should be 'SSPDB'
    HOST = os.getenv('HOST')                #insert from pod def, should be 'pg-db'
    PORT = os.getenv('PORT')                #insert from pod def, should be 5432


    #-------------------------------------

    #establish connection to db
    print('Establishing connection to database')
    print("postgresql://{user}:{pw}@{host}:{port}/{db}".format(host=HOST,port=PORT ,db=DB, user=USER, pw=PASSWORD))
    engine = create_engine("postgresql://{user}:{pw}@{host}:{port}/{db}".format(host=HOST,port=PORT ,db=DB, user=USER, pw=PASSWORD))
    #-------------------------------------

    #check to see if player table exist
    print('Checking to see if tables exist')
    df = pd.read_sql("SELECT table_name FROM information_schema.tables WHERE table_schema='public'", con=engine)
    if 'PLAYER_DATA' in df['Tables_in_SSPDB'].values:
        print('Table already exists')
        df2 = pd.read_sql('SELECT * FROM PLAYER_DATA', con=engine)
        pl=[]
        for i in df2.index:
            p=synthSportPlayer.player(int(df2.loc[i]['skill']),int(df2.loc[i]['variance']),df2.loc[i]['name'],int(df2.loc[i]['pointLimit']))
            p.totalPoints=int(df2.loc[i]['totalPoints'])
            if df2.loc[i]['pointRec']!='':
                p.pointRec=list(map(int,df2.loc[i]['pointRec'].split(':')))
            pl.append(p)
        print("Players re-constructed")

    else:
        print("Creating Table")
        engine.execute("""
        CREATE TABLE PLAYER_DATA (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(255), 
        skill INT(10), 
        variance INT(10),
        pointRec VARCHAR(255),
        totalPoints INT(10),
        pointLimit INT(10))""")

        print("Table created. Creating Players.")
        pl,tab = synthSportPlayer.generatePlayers(32)
        tab2=tab.copy()
        tab2.sort_index(inplace=True)
        tab2.drop('week_-1',axis=1,inplace=True)
        tab2["pointRec"]=''
        tab2["totalPoints"]=0
        tab2["pointLimit"]=10
        tab2.to_sql("PLAYER_DATA",engine,index=False,if_exists='append')
        print("Players created")
    #------------------------------------------
    if 'RANKING_DATA' in df['Tables_in_SSPDB'].values:
        logging.info('Table already exists')
        df3 = pd.read_sql('SELECT * FROM RANKING_DATA', con=engine)

    else:
        logging.info("Creating Table")
        engine.execute("""
        CREATE TABLE RANKING_DATA (
        rank_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        points INT(10),
        week VARCHAR(255))
        """)
        logging.info("Table created.")

    #------------------------------------------
    ls=synthSportPlayer.liveSeason(numPlayers=len(pl),players=pl)
    
    app.run(host='0.0.0.0',port=2001)                #tell the app to run setting the host and the port number
