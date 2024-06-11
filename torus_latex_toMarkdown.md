

```latex to Markdown Code

\documentclass{standalone}
\usepackage{pgfplots}
\pgfplotsset{compat=newest}
\begin{document}
\begin{tikzpicture}
\begin{axis}[]
\addplot3[
    surf,
    samples=50,
    domain=0:2*pi,
    y domain=0:2*pi,
    z buffer=sort,
    colormap/cool,
] (
    {(2+cos(deg(x)))*cos(deg(y))}, % x(t,s)
    {(2+cos(deg(x)))*sin(deg(y))}, % y(t,s)
    {sin(deg(x))}                  % z(t,s)
);
\end{axis}
\end{tikzpicture}
\end{document}
