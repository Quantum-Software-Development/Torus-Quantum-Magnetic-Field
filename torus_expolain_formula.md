In this formula, ( R ) represents the radius from the center of the torus tube to the center of the torus, ( r ) is the radius of the tube, and ( u, v ) are the parameters that vary along the angles of the torus. If you need any further explanation or help with LaTeX, I’m at your disposal.

<!--
The hexadecimal code for GitHub blue is #0366d6. To apply this color in a LaTeX formula, you can use the xcolor package in LaTeX. Here is an example of how you can define the color and use it in the torus formula:
-->
#

$$\begin{align*}
x(\theta, \phi) &= (R + r \cos \theta) \cos \phi \\
y(\theta, \phi) &= (R + r \cos \theta) \sin \phi \\
z(\theta, \phi) &= r \sin \theta
\end{align*}$$

#

 begin{align*}
x(\theta, \phi) &= (R + r \cos \theta) \cos \phi \\
y(\theta, \phi) &= (R + r \cos \theta) \sin \phi \\
z(\theta, \phi) &= r \sin \theta
\end{align*}

#


$$\documentclass{article}
\usepackage{xcolor} % Package for colors

\definecolor{githubblue}{HTML}{0366d6} % Defining the GitHub blue color

\begin{document}

\[
\color{githubblue}
\begin{align*}
x(u, v) &= (R + r \cos v) \cos u \\
y(u, v) &= (R + r \cos v) \sin u \\
z(u, v) &= r \sin v
\end{align*}
\]

\end{document}$$

