from math import*
m_b_c = 30
u_t = True
u_ta = False
Data = True

if u_t or u_ta:
    if not(u_t and not Data):
        if (u_t):
            m_b_c += 11
        elif (Data):
            m_b_c += 2
        else:
            m_b_c += 33
if u_ta or Data:
    if not u_t or (not Data and u_ta) or u_ta:
        m_b_c += 40
    else:
        m_b_c += 50
print(m_b_c)