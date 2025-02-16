import asyncio
from telethon import TelegramClient, events, sync, types , Button
from telethon import functions
from telethon.tl.types import *
import time
import pickle

# Use your own values from my.telegram.org
api_id = 29068923
api_hash = '72035fc7d10fc5bd2847e23ecad1a850'
bot_token = "7515175700:AAHmCsUMsmKH_VfFNQJAVIkdMw2h2RZN8B8"
client = TelegramClient("bot-chisme",api_id,api_hash).start(bot_token=bot_token)

print("Iniciando")

#lista de mensajes
lista_1=[]

#lista de administradores
adm=[968663996,847369429,1193174186]

#lista de usuarios:
usuarios=[]

#fichero=open("usuarios.dat","wb")
#pickle.dump(usuarios,fichero)
#fichero.close()


#grupo de administradores
grupo_adm=-1002286030144

#codigos de los topics del canal
FMFC=2
FQF=7 
FIMI=8
FH=9
FCS=10
FC=11
FCE=12
FCA=13
FCF=15
FEM=16
FEI=17
FIE=18
UCM=130

#############Funcion de cartas para un 14 de febrero########
#cartas=[]

#fichero=open("cartas.txt","wb")
#pickle.dump(cartas,fichero)
#fichero.close()

ayuda="1-Para suscribirte al bot puedes usar el comando /sub y a continuacion escribes las siglas en mayusculas de la facultad a la que perteneces y al final ':'\n*Ejemplo:\n/sub FMFC:\n/sub UCM:\nTambien puedes suscribirte con el boton 'Suscribirte' y siguiendo las instrucciones.Esta accion es irreversible, por favor ten mucho cuidado a cual te unes.\n2-Para enviar mensajes al canal primero debes estar suscrito, solo escribe el mensaje a enviar y te saldra el mensaje con botones para enviar; tambien pueden usar los siguientes comandos: \n/enviar 'mensaje a enviar'\n*Ejemplo: \n/enviar Te tengo un chisme nuevo \n2.1-Para enviar una cancion 🎧 o foto 📸 se realiza el mismo procedimiento, se envia al chat y te saldran los botones para enviar; o utiliza el mismo comando, ademas se puede responder una foto o cancion con el comando /enviar *'Mensaje a enviar' \n*Ejemplo: \n(responde una foto o cancion y luego escribe en el chat) \n/enviar *Aqui mando una cancion para mi persona especial \n3-Vuelvo a recalcar, PARA ENVIAR MENSAJES DEBES ESTAR SUSCRITO AL BOT EN UNA DE LAS FACULTADES EXISTENTES.\n4-Si tienes alguna queja o sugerencia usa el comando /feedback, funciona igual que /enviar o puedes escribir un mensaje y enviarlo como feedback con su respectivo boton\n5-Para unirte al canal usa el comando /canal"

async def buscador(mesage):
    #buscador
    indexfmfc=mesage.find("FMFC:")
    indexfqf=mesage.find("FQF:")
    indexfimi=mesage.find("FIMI:")
    indexfh=mesage.find("FH:")
    indexfcs=mesage.find("FCS:")
    indexffc=mesage.find("FC:")
    indexfce=mesage.find("FCE:")
    indexfca=mesage.find("FCA:")
    indexfcf=mesage.find("FCF:")
    indexfem=mesage.find("FEM:")
    indexfei=mesage.find("FEI:")
    indexfie=mesage.find("FIE:")
    indexucm=mesage.find("UCM:")
    
    codigo=0
    indexplus=0
    ini=""
    
    if(indexfmfc>0):
        codigo=FMFC
        indexplus=4
        ini="FMFC"
    elif(indexfqf>0):
        codigo=FQF
        indexplus=3
        ini="FQF"
    elif(indexfimi>0):
        codigo=FIMI
        indexplus=4
        ini="FIMI"
    elif(indexfh>0):
        codigo=FH
        indexplus=2
        ini="FH"
    elif(indexfcs>0):
        codigo=FCS
        indexplus=3
        ini="FCS"
    elif(indexffc>0):
        codigo=FC
        indexplus=2
        ini="FC"
    elif(indexfce>0):
        codigo=FCE
        indexplus=3
        ini="FCE"
    elif(indexfca>0):
        codigo=FCA
        indexplus=3
        ini="FCA"
    elif(indexfcf>0):
        codigo=FCF
        indexplus=3
        ini="FCF"
    elif(indexfem>0):
        codigo=FEM 
        indexplus=3
        ini="FEM"
    elif(indexfei>0):
        codigo=FEI
        indexplus=3
        ini="FEI"
    elif(indexfie>0):
        codigo=FIE
        indexplus=3
        ini="FIE"
    elif(indexucm>0):
        codigo=UCM
        indexplus=3
        ini="UCM"
        
    lista=[codigo,indexplus,ini]
    
    return lista

async def estasub(id):
    fichero=open("usuarios.dat","rb")
    usuarios=pickle.load(fichero)
    fichero.close()
    lista=[]
    sub=False
    ban=False
    for user in usuarios:
        if id==user["id"]:
            sub=True
            facu=user["facu"]
            ban=user["ban"]
            lista.append(sub)
            lista.append(facu)
            lista.append(ban)
            return lista
    lista.append(sub)
    lista.append(False)
    lista.append(ban)
    return lista


@client.on(events.NewMessage)
async def handle_new_message(event):
    sender = await event.get_sender()
    chat = await event.get_chat()
    mesage=event.message.message
    canal=-1002357728979
    chanel=await client.get_entity(PeerChannel(canal))
    source_adm=await client.get_entity(PeerChannel(grupo_adm))
    #print(sender.id)
    #print(chat)
    lista= await buscador(mesage)
    sub_1= await estasub(sender.id)
    
    #Comando /help para la ayuda
    if(mesage=="/help" and sub_1[2]==False):
        if(sub_1[0]):
            await client.send_message(chat, message=ayuda,buttons=[
                Button.text("Ayuda",resize=True,single_use=False),
                Button.text("Grupo",resize=True,single_use=False)
                ])
        else:
            await client.send_message(chat, message=ayuda,buttons=[
                Button.text("Ayuda",resize=True,single_use=False),
                Button.text("Grupo",resize=True,single_use=False),
                Button.text("Suscribirse",resize=True,single_use=True)
                ])
    
    elif(mesage=="Grupo"):
        if(sub_1[0]):
            await client.send_message(chat, message="Link del grupo de Secretos y Confesiones 🤫: https://t.me/+TDziJX0csZRmOTQx",buttons=[
                Button.text("Ayuda",resize=True,single_use=False),
                Button.text("Grupo",resize=True,single_use=False)
                ])
        else:
            await client.send_message(chat, message="Link del grupo de Secretos y Confesiones 🤫: https://t.me/+TDziJX0csZRmOTQx",buttons=[
                Button.text("Ayuda",resize=True,single_use=False),
                Button.text("Grupo",resize=True,single_use=False),
                Button.text("Suscribirse",resize=True,single_use=True)
                ])
            
    elif(mesage=="Ayuda"):
        if(sub_1[0]):
            await client.send_message(chat, message=ayuda,buttons=[
                Button.text("Ayuda",resize=True,single_use=False),
                Button.text("Grupo",resize=True,single_use=False)
                ])
        else:
            await client.send_message(chat, message=ayuda,buttons=[
                Button.text("Ayuda",resize=True,single_use=False),
                Button.text("Grupo",resize=True,single_use=False),
                Button.text("Suscribirse",resize=True,single_use=True)
                ])
        
    #Comando /start se dispara con la primera interaccion con el bot
    elif(mesage=="/start"):
        if(sub_1[0]):
            await client.send_message(chat,"Hola! escribe /help para obtener ayuda de como enviar mensajes al grupo de tu facultad",buttons=[
                Button.text("Ayuda",resize=True,single_use=False),
                Button.text("Grupo",resize=True,single_use=False)
                ])
        else:
            await client.send_message(chat,"Hola! escribe /help para obtener ayuda de como enviar mensajes al grupo de tu facultad",buttons=[
                Button.text("Ayuda",resize=True,single_use=False),
                Button.text("Grupo",resize=True,single_use=False),
                Button.text("Suscribirse",resize=True,single_use=True)
                ])
            
    elif(mesage=="Suscribirse" and sub_1[2]==False):
        await client.send_message(chat,"Elige la facultad donde deseas suscribirte, esta accion no se puede deshacer, fijate bien cual boton precionas...",buttons=[
            [Button.text("🧮 FMFC:",resize=True,single_use=True),
            Button.text("🔬 FQF:",resize=True,single_use=True),
            Button.text("🚂 FIMI:",resize=True,single_use=True),
            Button.text("📚 FH:",resize=True,single_use=True),
            Button.text("🧠 FCS:",resize=True,single_use=True)],
            [Button.text("🏠 FC:",resize=True,single_use=True),
            Button.text("💸 FCE:",resize=True,single_use=True),
            Button.text("🦮 FCA:",resize=True,single_use=True),
            Button.text("⚽️ FCF:",resize=True,single_use=True),
            Button.text("💼 FEM:",resize=True,single_use=True)],
            [Button.text("👶 FEI:",resize=True,single_use=True),
            Button.text("🤖 FIE:",resize=True,single_use=True),
            Button.text("🩺 UCM:",resize=True,single_use=True)]
        ])
    
    elif not (sub_1[0]) and (lista[0]!=0) and (sub_1[2]==False):
        index=mesage.find(" ")
        newuser={"id":sender.id,"facu":lista[2],"ban":False}
        fichero=open("usuarios.dat","rb")
        usuarios=pickle.load(fichero)
        fichero.close()
        sub=False
        for user in usuarios:
            if(user==newuser):
                await event.reply("Ya estas Suscrito al bot en la facultad de: " + mesage[index:len(mesage)-1],buttons=[
                    Button.text("Ayuda",resize=True,single_use=False),
                    Button.text("Grupo",resize=True,single_use=False)
                ])
                sub=True
        if not (sub):
            usuarios.append(newuser)
            await event.reply("Te has Suscrito al bot en la facultad de: " + mesage[index:len(mesage)-1],buttons=[
                Button.text("Ayuda",resize=True,single_use=False),
                Button.text("Grupo",resize=True,single_use=False)
            ])
            fichero=open("usuarios.dat","wb")
            pickle.dump(usuarios,fichero)
            fichero.close()
        
    elif(mesage[0:5] == "/sub " and sub_1[2]==False):
        if(lista[0]!=0):
            index=mesage.find(" ")
            newuser={"id":sender.id,"facu":lista[2],"ban":False}
            fichero=open("usuarios.dat","rb")
            usuarios=pickle.load(fichero)
            fichero.close()
            sub=False
            for user in usuarios:
                if(user==newuser):
                    await event.reply("Ya estas Suscrito al bot en la facultad de: " + mesage[index:len(mesage)-1],buttons=[
                        Button.text("Ayuda",resize=True,single_use=False),
                        Button.text("Grupo",resize=True,single_use=False)
                    ])
                    sub=True
            if not (sub):
                usuarios.append(newuser)
                await event.reply("Te has Suscrito al bot en la facultad de: " + mesage[index:len(mesage)-1],buttons=[
                    Button.text("Ayuda",resize=True,single_use=False),
                    Button.text("Grupo",resize=True,single_use=False)
                ])
                fichero=open("usuarios.dat","wb")
                pickle.dump(usuarios,fichero)
                fichero.close()
        else:
            await client.send_message(chat,message="Formato de suscriccion erronea, consulte la ayuda con el comando /help")
    
    elif(mesage[0:7] == "/desub " and adm.index(sender.id) != -1):
        index=mesage.find(" ")
        text=mesage.strip()
        fichero=open("usuarios.dat","rb")
        usuarios=pickle.load(fichero)
        fichero.close()
        sub=False
        for user in usuarios:
            if(str(user["id"])==str(text[index+1:])):
                usuarios.remove(user)
                await event.reply("Se ha desuscrito al usuario")
                sub=True
        if not (sub):
            await event.reply("No se encontro el usuario, error en el id")
        fichero=open("usuarios.dat","wb")
        pickle.dump(usuarios,fichero)
        fichero.close()
        
    elif(sub_1[0] and sub_1[2]==False):
        
        if(mesage[0:8] == "/enviar "):
            if(event.message.media):
                if isinstance(event.message.media, MessageMediaPhoto):
                    index=mesage.find(" ")
                    text=mesage[index+1:]
                    text=text.replace("pinga","p*nga")
                    text=text.replace("cojone","coj*ne")
                    text=text.replace("bollo","b*llo")
                    text=text.replace("negga","n*gga")
                    text=text.replace("singao","s*ngao")
                    text=text.replace("singar","s*ngar")
                    await client.send_message(source_adm, file=event.message.media.photo, message=sub_1[1]+":"+text,buttons=[
                        Button.inline("Aprobar",data='done')
                    ])
                    await event.reply("Foto y mensaje enviado al administrador 🚀 si es aprobado se enviara al canal 😉")
                    user={"id":sender.id,"mess":sub_1[1]+":"+text[:len(text)-3]}
                    lista_1.append(user)
            
            elif isinstance(event.message.media, MessageMediaDocument):
                index=mesage.find(" ")
                text=mesage[index+1:]
                text=text.replace("pinga","p*nga")
                text=text.replace("cojone","coj*ne")
                text=text.replace("bollo","b*llo")
                text=text.replace("negga","n*gga")
                text=text.replace("singao","s*ngao")
                text=text.replace("singar","s*ngar")
                await client.send_message(source_adm, file=event.message.media.document, message=sub_1[1]+":"+text,buttons=[
                    Button.inline("Aprobar",data='done')
                ])
                await event.reply("Foto y mensaje enviado al administrador 🚀 si es aprobado se enviara al canal 😉")
                user={"id":sender.id,"mess":sub_1[1]+":"+text[:len(text)-3]}
                lista_1.append(user)
        
            elif(mesage[0:9] == "/enviar *" and event.message.reply_to):
                reply_to_msg_id = event.message.reply_to.reply_to_msg_id
                reply_to_peer_id = event.message.reply_to.reply_to_peer_id
                original_message = await client.get_messages(reply_to_peer_id, ids=reply_to_msg_id)
                text=original_message.message
                index=mesage.find("*")
                if(original_message.media):
                    if isinstance(original_message.media, MessageMediaPhoto):
                        await client.send_message(source_adm, file=original_message.media.photo, message=sub_1[1]+ ":"+mesage[index+1:],buttons=[
                            Button.inline("Aprobar",data='done')
                        ])
                        await event.reply("Foto y mensaje enviado al administrador 🚀 si es aprobado se enviara al canal 😉")
                        user={"id":event.sender.id,"mess":sub_1[1]+ ":"+mesage[index+1:]}
                        lista_1.append(user)
                    elif isinstance(original_message.media, MessageMediaDocument):
                        await client.send_message(source_adm, file=original_message.media.document, message=sub_1[1]+ ":"+mesage[index+1:],buttons=[
                            Button.inline("Aprobar",data='done')
                        ])
                        await event.reply("Cancion y mensaje enviado al administrador 🚀 si es aprobado se enviara al canal 😉")
                        user={"id":event.sender.id,"mess":sub_1[1]+ ":"+mesage[index+1:]}
                        lista_1.append(user)
                else:
                    await client.send_message(source_adm, message=sub_1[1]+ ":"+text,buttons=[
                            Button.inline("Aprobar",data='done')
                        ])
                    await event.reply("Mensaje enviado al administrador 🚀, si es aprobado se enviara al canal 😉")
                    user={"id":event.sender.id,"mess":sub_1[1]+ ":"+text}
                    lista_1.append(user)
             
            else:
                index=mesage.find(" ")
                text=mesage[index+1:]
                text=text.replace("pinga","p*nga")
                text=text.replace("cojone","coj*ne")
                text=text.replace("bollo","b*llo")
                text=text.replace("negga","n*gga")
                text=text.replace("singao","s*ngao")
                text=text.replace("singar","s*ngar")
                await client.send_message(source_adm,sub_1[1]+ ":"+text,buttons=[
                    Button.inline("Aprobar",data='done')
                ])
                await event.reply("Mensaje enviado al administrador 🚀, si es aprobado se enviara al canal 😉")
                user={"id":event.sender.id,"mess":sub_1[1]+ ":"+text}
                lista_1.append(user)
                
        elif(mesage=="/grupo"):
            await event.reply("Link del grupo de Secretos y Confesiones 🤫: https://t.me/+TDziJX0csZRmOTQx")
            
        elif(mesage=="/done" and event.message.reply_to and adm.index(sender.id) != -1):
            reply_to_msg_id = event.message.reply_to.reply_to_msg_id
            reply_to_peer_id = event.message.reply_to.reply_to_peer_id
            original_message = await client.get_messages(chat, ids=reply_to_msg_id)
            text="-" + original_message.message
            lista2=await buscador(text)
            if(original_message.media and lista2[1]>1):
                if isinstance(original_message.media, MessageMediaPhoto):
                    await client.send_message(chanel , file=original_message.media.photo , message=text, reply_to=lista2[0])
                    await event.reply("Foto enviada al canal")
                elif isinstance(original_message.media, MessageMediaDocument):
                    await client.send_message(chanel , file=original_message.media.document , message=text, reply_to=lista2[0])
                    await event.reply("Cancion enviada al canal")
                #elif (original_message.poll):
                #    await client.send_message(chanel, file=original_message.poll , message="", reply_to=lista[0])
                #    await event.reply("Encuesta enviada al canal")
            else:
                await client.send_message(chanel,message= text ,reply_to=lista2[0])
                await event.reply("Mensaje enviado al canal")
            if(sender.id!=adm[0]):
                await event.reply("No eres administrador para usar este comando")
            
        elif(mesage[0:10] == "/feedback "):
            index=mesage.find(" ")
            text="Mensaje de feedback: "
            text=text + mesage[index+1:]
            await client.send_message(source_adm, text )
            await event.reply("Mensaje enviado al administrador, gracias por la sugerencia 😁")
            
        elif(mesage[0:4] == "/no " and event.message.reply_to and adm.index(sender.id) != -1 ):
            reply_to_msg_id = event.message.reply_to.reply_to_msg_id
            reply_to_peer_id = event.message.reply_to.reply_to_peer_id
            original_message = await client.get_messages(chat, ids=reply_to_msg_id)
            text=original_message.message
            index=mesage.find(" ")
            mensage="El mensaje: '" + text + "' no ha sido enviado porque: " + mesage[index+1:]
            for user in lista_1:
                if(user["mess"]==text):
                    id=user["id"]
                    await client.send_message(id,mensage)
                    await event.reply("Mensaje enviado")
                    lista_1.remove(user)
                
        elif(mesage == "/ban" and event.message.reply_to and adm.index(sender.id) != -1):
            reply_to_msg_id = event.message.reply_to.reply_to_msg_id
            reply_to_peer_id = event.message.reply_to.reply_to_peer_id
            original_message = await client.get_messages(chat, ids=reply_to_msg_id)
            text=original_message.message
            fichero=open("usuarios.dat","rb")
            usuarios=pickle.load(fichero)
            fichero.close()
            ban=False
            id=0
            for user in lista_1:
                if(user["mess"]==text):
                    id=user["id"]
            for user in usuarios:
                if(str(user["id"])==str(id)):
                    newuser={"id":user["id"],"facu":user["facu"],"ban":True}
                    usuarios.remove(user)
                    usuarios.append(newuser)
                    fichero2=open("usuarios.dat","wb")
                    pickle.dump(usuarios,fichero2)
                    fichero2.close()
                    await client.send_message(chat,message="Usuario muteado")
                    ban=True
            if not (ban):
                client.send_message(chat,message="Usuario no encontrado, problema de id")
            
       
        else:
            if not isinstance(chat,Channel) and sub_1[2]==False:
                botones=[
                    [Button.inline("Enviar mensaje",data='mensaje'), Button.inline("Enviar Feedback",data='feed')]
                ]
                if(event.message.media):
                    if isinstance(event.message.media, MessageMediaPhoto):
                        await client.send_message(chat,message="El mensaje:\n"+mesage+"\n\n Lo quiere enviar?", file=event.message.media.photo ,buttons=botones)
                    elif isinstance(event.message.media, MessageMediaDocument):
                        await client.send_message(chat,message="El mensaje:\n"+mesage+"\n\n Lo quiere enviar?", file=event.message.media.document ,buttons=botones)
                else:
                    await event.respond("El mensaje:\n"+mesage+"\n\n Lo quiere enviar?" ,buttons=botones)
        
    else:
        if not isinstance(chat,Channel):
                await client.send_message(chat,"No esta suscrito al bot, si tiene dudas presione /help")
                
            #Funcion de mandar encuestas
    #elif(event.message.poll):
    #    await event.reply("Encuesta recibida y enviada al administrador 🚀 , si es aprobada se enviara al canal 😉")
    #    await client.send_message(source_adm , file=event.poll , message="" )
      
        '''  
        Funcion de carta
    elif(mesage[0:7]== "/carta "):
        index=mesage.find("Para:")
        if(index>20):
            fichero=open("cartas.txt","rb")
            cartas=pickle.load(fichero)
            fichero.close()
            cartas.append(mesage[7:])
            fichero2=open("cartas.txt","wb")
            pickle.dump(cartas,fichero2)
            fichero2.close()
            await event.reply("Carta enviada 🚀, se guardara hasta el 14 de febrero y luego sera abierta")
        else:
            await event.reply("Texto de carta muy corto o no se ha encontrado el 'Para:'")
    
    
    
    elif(mesage == "/abrir" and sender.id == 968663996):
        await event.reply("Se ha abierto el buzon, se enviaran todas las cartas al canal")
        fichero=open("cartas.txt","rb")
        cartas=pickle.load(fichero)
        fichero.close()
        for carta in cartas:
            await client.send_message(chanel, message=carta)
            
    elif(mesage=="/num"):
        fichero=open("cartas.txt","rb")
        cartas=pickle.load(fichero)
        fichero.close()
        await event.reply("En este momento se encuentran " + str(len(cartas)) + " cartas en el buzon")
        
        '''
        
@client.on(events.CallbackQuery(data='mensaje'))
async def reenviar_mensaje_handler(event):
    sender = await event.get_sender()
    mesage=await event.get_message()
    canal=-1002357728979
    source_adm=await client.get_entity(PeerChannel(grupo_adm))
    sub_1= await estasub(sender.id)
    
    index_1=mesage.text.find(":")+2
    index_2=mesage.text.rfind("L")
    
    if(mesage.media):
        if(sub_1[2]==False):
                if isinstance(mesage.media, MessageMediaPhoto):
                    text=mesage.text[index_1:index_2]
                    text=text.replace("pinga","p*nga")
                    text=text.replace("cojone","coj*ne")
                    text=text.replace("bollo","b*llo")
                    text=text.replace("negga","n*gga")
                    text=text.replace("singao","s*ngao")
                    text=text.replace("singar","s*ngar")
                    await client.send_message(source_adm, file=mesage.media.photo, message=sub_1[1]+":"+text,buttons=[
                        Button.inline("Aprobar",data='done')
                    ])
                    await event.edit(mesage.text,buttons=Button.clear())
                    await event.reply("Foto y mensaje enviado al administrador 🚀 si es aprobado se enviara al canal 😉")
                    user={"id":sender.id,"mess":sub_1[1]+":"+text[:len(text)-3]}
                    lista_1.append(user)
            
                elif isinstance(mesage.media, MessageMediaDocument):
                    text=mesage.text[index_1:index_2]
                    text=text.replace("pinga","p*nga")
                    text=text.replace("cojone","coj*ne")
                    text=text.replace("bollo","b*llo")
                    text=text.replace("negga","n*gga")
                    text=text.replace("singao","s*ngao")
                    text=text.replace("singar","s*ngar")
                    await client.send_message(source_adm, file=mesage.media.document, message=sub_1[1]+":"+text,buttons=[
                        Button.inline("Aprobar",data='done')
                    ])
                    await event.edit(mesage.text,buttons=Button.clear())
                    await event.reply("Cancion y mensaje enviado al administrador 🚀 si es aprobado se enviara al canal 😉")
                    user={"id":sender.id,"mess":sub_1[1]+":"+text[:len(text)-3]}
                    lista_1.append(user)
             
    else:
        if(sub_1[2]==False):
                text=mesage.text[index_1:index_2]
                text=text.replace("pinga","p*nga")
                text=text.replace("cojone","coj*ne")
                text=text.replace("bollo","b*llo")
                text=text.replace("negga","n*gga")
                text=text.replace("singao","s*ngao")
                text=text.replace("singar","s*ngar")
                await client.send_message(source_adm,message=sub_1[1]+":"+text,buttons=[
                    Button.inline("Aprobar",data='done')
                ])
                await event.edit(mesage.text,buttons=Button.clear())
                await event.reply("Mensaje enviado al administrador 🚀, si es aprobado se enviara al canal 😉")
                user={"id":sender.id,"mess":sub_1[1]+":"+text[:len(text)-3]}
                lista_1.append(user)
    
@client.on(events.CallbackQuery(data='feed'))
async def reenviar_mensaje_handler(event):
    sender = await event.get_sender()
    sub_1= await estasub(sender.id)
    if(sub_1[2]==False):
        mesage=await event.get_message()
        source_adm=await client.get_entity(PeerChannel(grupo_adm))
        text="Mensaje de feedback: "
        index_1=mesage.text.find(":")
        index_2=mesage.text.rfind("L")
        text=text + mesage.text[index_1:index_2]
        await client.send_message(source_adm, text )
        await event.reply("Mensaje enviado al administrador, gracias por la sugerencia 😁")
    
@client.on(events.CallbackQuery(data='done'))
async def reenviar_mensaje_handler(event):
    sender = await event.get_sender()
    mesage=await event.get_message()
    canal=-1002357728979
    chanel=await client.get_entity(PeerChannel(canal))
    
    
    text="-" + mesage.text
    lista2=await buscador(text)
    if(mesage.media and lista2[1]>1):
        if isinstance(mesage.media, MessageMediaPhoto):
            await client.send_message(chanel , file=mesage.media.photo , message=text, reply_to=lista2[0])
            #await event.reply("Foto enviada al canal")
            await event.edit(mesage.text+"\n \n"+"Mensaje enviado")
        elif isinstance(mesage.media, MessageMediaDocument):
            await client.send_message(chanel , file=mesage.media.document , message=text, reply_to=lista2[0])
            #await event.reply("Cancion enviada al canal")
            await event.edit(mesage.text+"\n \n"+"Mensaje enviado")
                #elif (original_message.poll):
                #    await client.send_message(chanel, file=original_message.poll , message="", reply_to=lista[0])
                #    await event.reply("Encuesta enviada al canal")
    else:
        await client.send_message(chanel,message= text ,reply_to=lista2[0])
        #await event.reply("Mensaje enviado al canal")
        await event.edit(mesage.text+"\n \n"+"Mensaje enviado")
    
         
with client:
    client.run_until_disconnected()