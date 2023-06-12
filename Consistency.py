import streamlit as st
from streamlit_extras.colored_header import colored_header
from PIL import Image

st.title('Data Quality Spotlight')
colored_header(
    label="Consistency👯‍♀️",
    description="10 minute read. For questions contact Jordan @ DataGovernance@perkinscoie.com",
    color_name="red-70",
)

"Have you ever watched a movie and noticed a glaring continuity error? Maybe Forrest Gump buying Apple stocks in 1975, the car in the Lord of the Rings, Bradley Cooper holding a fake baby. One moment, you're immersed in the Land of Oz, and the next, you're noticing every time Dorothy's hair grows and shrinks a few inches between shots."
chat_image = Image.open('JUNE-DL-img21.png')
st.image(chat_image) 
"There's something funny about our awareness of continuity errors in film. The fact that Harry Potter could fly on a broomstick didn't raise any flags for me, but seeing the bike seat on the broomstick is a glaring error."
"Much like the world-building in a Hollywood movie, we are not focused on real-world accuracy when we measure Consistency. Rather, we are focused on if the information matches up across systems.   "
":red[__Consistency__] measures whether data is the same, in format and in value, across multiple instances. Consistency is an important dimension of data quality because it allows our data to talk to one another.  "
"If this is starting to sound familiar, great! Consistency is closely related to the data quality dimension we explored in our last module: accuracy."
' (See here: Streamlit (https://jordangalvin05-data-quality-a-quality-spotlight-accuracy-yxs8rp.streamlit.app/)'
"To distinguish the accuracy and consistency, let's start with a quick recap of accuracy.  "
''
st.expander('Expander')
acc_image = Image.open('JUNE-DL-img22.png')
with st.expander('Define Accuracy!'):
    st.image(acc_image)
'__Accuracy__ measures whether the data matches the actual or “real world” value. For example: the data says my name is Anna and my name actually is Anna. ',

'__Another example__ My office is listed as SEA, but I actually work in CHI.'

st.expander('Expander')
with st.expander('Define Consistency!'):
    con_image = Image.open('JUNE-DL-img23.png')
    st.image(con_image)
'__Consistency__, on the other hand, measures whether the data matches the same values across the firm. For example, consistent data would mean that my name is listed as Anna in different data sets throughout the firm.   '
' __Another example__ My office is listed as SEA, Seattle, and HQ across different systems. '
''
world_image = Image.open('JUNE-DL-img24.png')
st.image(world_image) 
'__Data may be consistent but also inaccurate!__ What would this look like? All of our firm systems may list my name is Anna, but my name may actually be Jordan. For this reason, we need to consider all the dimensions of data quality when assessing our data.  '
''
'Inconsistent data is common when dealing with multiple systems, making it challenging to link systems to one another and get values to match up. '
'How do we make sure our data is consistent? One helpful tool is our data catalog, which will be live next month (stay tuned!). We work with Data Stewards to make sure our data is clearly described, and make it simple to trace the data lineage.  '


'__Question 1.__   Which of the statements shows an issue with consistency?'
if st.checkbox("The client's address is misspelled in their system."):
    st.write('Not quite – try again.')
if st.checkbox("I am not sure where to go for the most up-to-date address for the client. "):
    st.write('Not quite – try again.')
if st.checkbox("Department A and Department B have different addresses for the client."): 
    st.write('Great job! That is correct.')
if st.checkbox("We do not have a process to share address changes between teams. "):
    st.write('Not quite – try again.')
'The good news is, Data Governance can help you with all of these challenges and more.'
st.expander('Expander')
with st.expander('Recap and Review!'):
    st.write('__1.__ Consistency = measure of whether data is the same across systems.')
    st.write('__2.__ Accuracy = measure of whether data is correct.')
    st.write('__3.__ Each dimension contributes to our assessment of data quality. We want our data to be both consistent and accurate. ')
''
'Thank you for reading along! As always, the Data Governance team is here to support you on your data literacy journey. If you have any questions, please reach out to us at DataGovernance@perkinscoie.com. Happy June! '
''
''
'Have feedback on the new format? Please let us know via email or by clicking feedback at the end of the intial communication. '
