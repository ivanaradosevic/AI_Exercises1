#12. Nađite sva ponavljanja ‘stol’ u zadanom stringu zanemarujući velika i mala slova:
# „U kuhinji je stol. STOL je novi.”

a= "U kuhinji je stol. STOL je novi."
b= a.lower()
print(b.count("stol"))

#moram prvo sva slova pretvoriti u mala lower da bi prepoznao string


