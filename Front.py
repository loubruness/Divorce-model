import streamlit as st
import requests

st.text("Do you want to find out if you and your significant other will divorce or break up ?")
st.text("Find out with our love expert AI !")

st.text("      ")
st.text("      ")
st.text("For each question, answer with the following scale :")
st.text("0=Never, 1=Seldom, 2=Averagely, 3=Frequently, 4=Always")

st.text("      ")
st.text("      ")

with st.form(key='my_form'):
    A1 =  st.slider("Q1 : If one of us apologizes when our discussion deteriorates, the discussion ends.",max_value=4)

    A2 =  st.slider("Q2 : I know we can ignore our differences, even if things get hard sometimes.",max_value=4)

    A3 =  st.slider("Q3 : When we need it, we can take our discussions with my significant other from the beginning and correct it.",max_value=4)

    A4 =  st.slider("Q4 : When I discuss with my partner, to contact them will eventually work.",max_value=4)

    A5 =  st.slider("Q5 : The time I spend with my significant other is special for us.",max_value=4)

    A6 =  st.slider("Q6 : We don't have time at home as partners.",max_value=4)

    A7 =  st.slider("Q7 : We are like two strangers who share the same environment at home rather than family.",max_value=4)

    A8 =  st.slider("Q8 : I enjoy our holidays with my significant other.",max_value=4)

    A9 =  st.slider("Q9 : I enjoy traveling with my partner.",max_value=4)

    A10 =  st.slider("Q10 : Most of our goals are common to my significant other.",max_value=4)

    A11 =  st.slider("Q11 : I think that one day in the future, when I look back, I see that my partner and I have been in harmony with each other.",max_value=4)

    A12 =  st.slider("Q12 : My significant other and I have similar values in terms of personal freedom.",max_value=4)

    A13 =  st.slider("Q13 : My partner and I have similar sense of entertainment.",max_value=4)

    A14 =  st.slider("Q14 : Most of our goals for people (children, friends, etc.) are the same.",max_value=4)

    A15 =  st.slider("Q15 : Our dreams with my significant other are similar and harmonious.",max_value=4)

    A16 =  st.slider("Q16 : We're compatible with my partner about what love should be.",max_value=4)

    A17 =  st.slider("Q17 : We share the same views about being happy in our life with my significant other.",max_value=4)

    A18 =  st.slider("Q18 : My partner and I have similar ideas about how marriage should be.",max_value=4)

    A19 =  st.slider("Q19 : My significant other and I have similar ideas about how roles should be in marriage.",max_value=4)

    A20 =  st.slider("Q20 : My partner and I have similar values in trust.",max_value=4)

    A21 =  st.slider("Q21 : I know exactly what my significant other likes.",max_value=4)

    A22 =  st.slider("Q22 : I know how my partner wants to be taken care of when they're sick.",max_value=4)

    A23 =  st.slider("Q23 : I know my significant other's favorite food.",max_value=4)

    A24 =  st.slider("Q24 : I can tell you what kind of stress my partner is facing in their life.",max_value=4)

    A25 =  st.slider("Q25 : I have knowledge of my significant other's inner world.",max_value=4)

    A26 =  st.slider("Q26 : I know my partner's basic anxieties.",max_value=4)

    A27 =  st.slider("Q27 : I know what my significant other's current sources of stress are.",max_value=4)

    A28 =  st.slider("Q28 : I know my partner's hopes and wishes.",max_value=4)

    A29 =  st.slider("Q29 : I know my significant other very well.",max_value=4)

    A30 =  st.slider("Q30 : I know my partner's friends and their social relationships.",max_value=4)

    A31 =  st.slider("Q31 : I feel aggressive when I argue with my significant other.",max_value=4)

    A32 =  st.slider("Q32 : When discussing with my partner, I usually use expressions such as ‘you always’ or ‘you never’.",max_value=4)

    A33 =  st.slider("Q33 : I can use negative statements about my significant other's personality during our discussions.",max_value=4)

    A34 =  st.slider("Q34 : I can use offensive expressions during our discussions.",max_value=4)

    A35 =  st.slider("Q35 : I can insult my partner during our discussions.",max_value=4)

    A36=  st.slider("Q36 : I can be humiliating when we discuss.",max_value=4)

    A37 =  st.slider("Q37 : My discussion with my significant other is not calm.",max_value=4)

    A38 =  st.slider("Q38 : I hate my partner's way of open a subject.",max_value=4)

    A39 =  st.slider("Q39 : Our discussions often occur suddenly.",max_value=4)

    A40 =  st.slider("Q40 : We're just starting a discussion before I know what's going on.",max_value=4)

    A41 =  st.slider("Q41 : When I talk to my significant other about something, my calm suddenly breaks.",max_value=4)

    A42 =  st.slider("Q42 : When I argue with my partner, I only go out and I don't say a word.",max_value=4)

    A43 =  st.slider("Q43 : I mostly stay silent to calm the environment a little bit.",max_value=4)

    A44 =  st.slider("Q44 : Sometimes I think it's good for me to leave home for a while.",max_value=4)

    A45 =  st.slider("Q45 : I'd rather stay silent than discuss with my significant other.",max_value=4)

    A46 =  st.slider("Q46 : Even if I'm right in the discussion, I stay silent to hurt my partner.",max_value=4)

    A47 =  st.slider("Q47 : When I discuss with my significant other, I stay silent because I am afraid of not being able to control my anger.",max_value=4)

    A48 =  st.slider("Q48 : I feel right in our discussions.",max_value=4)

    A49 =  st.slider("Q49 : I have nothing to do with what I've been accused of.",max_value=4)

    A50 =  st.slider("Q50 : I'm not actually the one who's guilty about what I'm accused of.",max_value=4)

    A51 =  st.slider("Q51 : I'm not the one who's wrong about problems at home.",max_value=4)

    A52 =  st.slider("Q52 : I wouldn't hesitate to tell my partner about their inadequacy.",max_value=4)

    A53 =  st.slider("Q53 : When I discuss, I remind my significant other of their inadequacy.",max_value=4)

    A54 =  st.slider("Q54 : I'm not afraid to tell my partner about their incompetence.",max_value=4)

    submit_button = st.form_submit_button(label='Submit')


if submit_button:
    input_features = {"X" : [[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21, A22, A23, A24, A25, A26, A27, A28, A29, A30, A31, A32, A33, A34, A35, A36, A37, A38, A39, A40, A41, A42, A43, A44, A45, A46, A47, 
    A48, A49, A50, A51, A52, A53, A54]]}
    
    api_url = "http://localhost:5000/predict"
    
    response = requests.post(api_url, json=input_features)
    
    if response.status_code == 200:
        prediction = response.json().get("prediction")
        if prediction == 0:
            st.write(f'     ')
            st.write(f'Your predicted score is: {prediction[0]}! Start looking for a divorce lawyer...')
        else:
            st.write(f'     ')
            st.write(f'Your predicted score is: {prediction[0]}! Congratulations, your marriage is safe!')
    else:
        st.write(f"Error: Unable to get prediction. Status code: {response.status_code}")
