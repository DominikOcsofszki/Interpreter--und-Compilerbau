# Impementieren Sie Lambda-Ausdrücke mit der Syntax:
# var -> body
# achten Sie darauf, dass die Ausdrücke ohne Klammersetzung Variablen zugewiesen werden können also f := x -> x*x sollte syntaktisch korrekt sein.
# Der Aufruf eines Lambda Ausdrucks "f" erfolgt durch
# f(val)
# Überarbeiten Sie Ihre Implementierung des "local" Statements so, dass rekursiv definierte Funktionen als lokale Variable möglich sind.
# Implementieren Sie in Ihrer Programmiersprache einen counter, also eine Funktion, die folgendes Verhalten zeigt:
#
# c := counter(0);
# c(1) -> 1
# c(1) -> 2
# c(1) -> 3
# c(2) -> 5
# c(3) -> 8

tokens_lambda = ['lambda']
# tokens_lambda = ['lambda']
t_lambda = r'->'
literals_komma=','

