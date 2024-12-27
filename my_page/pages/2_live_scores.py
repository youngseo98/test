import streamlit as st 

st.title('LiveScore')

import streamlit as st

# Data for each match
matches = [
    {
        "team_1": "사우샘프턴",
        "score_1": 0,
        "team_2": "웨스트햄",
        "score_2": 1,
        "team_1_logo": "https://dthumb-phinf.pstatic.net?src=https://sports-phinf.pstatic.net/team/wfootball/default/18.png&type=f28_28&refresh=1",
        "team_2_logo": "https://dthumb-phinf.pstatic.net?src=https://sports-phinf.pstatic.net/team/wfootball/default/43.png&type=f28_28&refresh=1",
        "status": "종료",  # "Ended"
        "record_url": "/game/2024122710050850323/relay",
        "video_url": "/game/2024122710050850323/video"
    },
    {
        "team_1": "노팅엄",
        "score_1": 1,
        "team_2": "토트넘",
        "score_2": 0,
        "team_1_logo": "https://dthumb-phinf.pstatic.net?src=https://sports-phinf.pstatic.net/team/wfootball/default/15.png&type=f28_28&refresh=1",
        "team_2_logo": "https://dthumb-phinf.pstatic.net?src=https://sports-phinf.pstatic.net/team/wfootball/default/19.png&type=f28_28&refresh=1",
        "status": "종료",  # "Ended"
        "record_url": "/game/2024122710050850321/relay",
        "video_url": "/game/2024122710050850321/video"
    },
    {
        "team_1": "뉴캐슬",
        "score_1": 3,
        "team_2": "애스턴 빌라",
        "score_2": 0,
        "team_1_logo": "https://dthumb-phinf.pstatic.net?src=https://sports-phinf.pstatic.net/team/wfootball/default/31.png&type=f28_28&refresh=1",
        "team_2_logo": "https://dthumb-phinf.pstatic.net?src=https://sports-phinf.pstatic.net/team/wfootball/default/2.png&type=f28_28&refresh=1",
        "status": "종료",  # "Ended"
        "record_url": "/game/2024122710050850319/relay",
        "video_url": "/game/2024122710050850319/video"
    },
    # Add more match data here...
]

# Streamlit layout to display the matches
st.title("Football Match Results")

for match in matches:
    # Display team names and logos
    col1, col2 = st.columns([1, 1])  # Use columns to align teams side by side
    with col1:
        st.image(match["team_1_logo"], width=28)
        st.write(match["team_1"])
        st.write(match["score_1"])
    
    with col2:
        st.image(match["team_2_logo"], width=28)
        st.write(match["team_2"])
        st.write(match["score_2"])

    # Match status (ended)
    st.markdown(f"**Status:** {match['status']}")

    # Buttons for record and video
    record_button = st.button("Record", key=match["record_url"])
    if record_button:
        st.write(f"Viewing record for: {match['team_1']} vs {match['team_2']}")

    video_button = st.button("Video", key=match["video_url"])
    if video_button:
        st.write(f"Viewing video for: {match['team_1']} vs {match['team_2']}")
    
    # Add a line break for the next match
    st.markdown("---")
