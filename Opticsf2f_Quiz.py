from caroline import Presentation

p = Presentation(
    logo="./presentation_files/Durham_University_Logo.png",
    leftHanded=True,
    drawingHelp="lines",
    drawingHelpIntensity=0.04,
    roundTableServer="https://roundtable.researchx3d.com",
    presentationServer="https://etotheipiequals.github.io/Opticsf2f/Opticsf2f_Quiz.html",
    authenticationToken="osagASfew8t31qNqfHQ3Gq",
)

# drawingHelp = ""  OR "lines"  OR  "dots"
# drawingHelpIntenisty = flaot [0,1] ; 0=white   1 = black

########################################
############# TITLE slide ##############
########################################

p.newSlide()

p.title("** QLM Quiz **")

p.makeGrid(3,3)

p.gridImage(0,1,"./Figures/dark_side.png", height = 400) 

p.gridIFrame(2,1,"./Figures/time.mp3")



p.newQuiz(#(d)
    questionImage="./Figures/Maxwell.jpg",
    questionText="##Which equation contains a new term introduced by Maxwell?",
    answersText=[
        r"$\nabla \cdot \mathbf{E}=\frac{\rho}{\varepsilon_0}$",
        r"$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$",
        r"$\nabla \cdot \mathbf{B} = 0$",
        r"$\nabla \times \mathbf{B} = \mu_0 ~\mathbf{j} + \varepsilon_0 \mu_0 \frac{\partial \mathbf{E}}{\partial t}$",
    ],
)

p.newQuiz(#(b)
    questionText="#If a plane wave is incident on a lens, the wave fronts in the focal plane are",
    answersText=[r"$({\rm a})$ Planar.",
                 r"$({\rm b})$ Diverging.",
                 r"$({\rm c})$ Converging."]
)

p.newQuiz(#(b)
    questionText="#If a collimated laser beam is incident on a lens, the wave fronts in the focal plane are",
    answersText=[r"$({\rm a})$ Planar.",
                 r"$({\rm b})$ Diverging.",
                 r"$({\rm c})$ Converging."]
)

p.newQuiz(#(a)
    questionText="#If a collimated laser beam is incident on a lens, the beam waist of the focal beam is",
    answersText=[r"$({\rm a})$ Before (upstream of) the focal plane.",
                 r"$({\rm b})$ In the focal plane.",
                 r"$({\rm c})$ Beyond (downstream of) the focal plane."]
)


p.newQuiz( # (c)
    questionImage="./Figures/fourier.png",
    questionText="##Which of the following is the Fourier transform of M?",
    answersImage=[
        "./Figures/Z.png",
        "./Figures/A.png",
        "./Figures/M.png",
        "./Figures/N.png",
        "./Figures/W.png",
        "./Figures/X.png",
    ],
)


########################################
#############  New slide  ##############
########################################

p.newSlide()

p.title("What Richard Feynman said!")

p.leftText(r"""
... you'll get down a drain,

... nobody has yet escaped,

... nobody knows how it can be like that.
           
           """)
p.rightIFrame("https://www.youtube.com/embed/41Jc75tQcB0?start=509&end=521", height=315)

p.save("./Opticsf2f_Quiz.html")




