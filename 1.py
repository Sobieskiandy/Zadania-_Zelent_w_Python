print("Witaj, zadam ci kilka pytań.")
Uczniowie = input("Ilu uczniów liczy wraz z tobą twoja klasa:")
Cukierki = input("Ile cukierków kupiła mama:")

x=int(Uczniowie)-1
x1=int(Cukierki)//x
print("Dasz każdemu koledze po "+str(x1)+" cukierków")
y=int(Cukierki)%x
print("Dla Jasia na wieczór zostanie "+str(y)+" cukierków.")