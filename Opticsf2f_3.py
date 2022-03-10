from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://opticsf2f.github.io/Opticsf2f_3.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
############# TITLE slide ##############
########################################

########################################
p.newSlide()
p.title("$N$-slit diffraction ")


p.rightIFrame("./Figures/SlitPhasor.html", height = 600)


p.save("./Opticsf2f_3.html")




