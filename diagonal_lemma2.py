#!/bin/python
import re

# We have to deal with strings in the different level of language (it is just technical details)
def one_level_down(p):
    p = p.replace('\\', '\\\\\\\\'); # Yes, I know how you feel here, I feel the same :-D
    p = p.replace('"', '\\"');
    return p;


# substitute "x" in the property "p_meta" (expressed in the meta-language), by the value of x_value
def substitute(p_meta, x_value):
    return re.sub(r'x', x_value, p_meta);

def diagonal(p_meta):
    return substitute(p_meta, one_level_down('"'+one_level_down(p_meta)+'"'));


# find a phi_meta (a expression phi expressed in the meta-language), where phi = p(phi_meta)
def find_phi_meta(p_meta):
    return 'diagonal(\"'+substitute(p_meta, "diagonal(x)")+'\")'


# Convert a property expressed in the meta-level, to the object-level
def meta_to_object(p_meta):
    if re.search(r'^(("[^"]*")*)([^"]*)x', p_meta):
        return lambda x2:eval(substitute(p_meta, x2));
    else:
        # If we don’t find x, it is just a expression and not really a property
        return eval(p_meta);

p_meta = "P(x)"; # A random property
phi_meta = find_phi_meta(p_meta)
print("phi_meta = " + phi_meta);
phi = meta_to_object(phi_meta)
print("phi = " + phi)

p_phi_meta = 'P('+one_level_down(phi_meta)+')'
print("p(phi_meta) = " + p_phi_meta)

# We have phi = p(phi_meta) !!
print(phi == p_phi_meta)

# Now, we can have some fun :-)
print("-"*50)
p_meta = "print(x)"
phi_meta = find_phi_meta(p_meta)
print("phi_meta = " + phi_meta);
p = meta_to_object(p_meta)

p(phi_meta) # p(phi_meta) = phi so basically, phi print itself !!
