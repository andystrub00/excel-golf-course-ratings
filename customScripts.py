import geocoder

state_mapping = {
    'Ala.': 'AL', 'Alaska': 'AK', 'Ariz.': 'AZ', 'Ark.': 'AR', 'Calif.': 'CA',
    'Colo.': 'CO', 'Conn.': 'CT', 'Del.': 'DE', 'Fla.': 'FL', 'Ga.': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Ill.': 'IL', 'Ind.': 'IN', 'Iowa': 'IA',
    'Kans.': 'KS', 'Ky.': 'KY', 'La.': 'LA', 'Maine': 'ME', 'Md.': 'MD',
    'Mass.': 'MA', 'Mich.': 'MI', 'Minn.': 'MN', 'Miss.': 'MS', 'Mo.': 'MO',
    'Mont.': 'MT', 'Neb.': 'NE', 'Nev.': 'NV', 'N.H.': 'NH', 'N.J.': 'NJ',
    'N.M.': 'NM', 'N.Y.': 'NY', 'N.C.': 'NC', 'N.D.': 'ND', 'Ohio': 'OH',
    'Okla.': 'OK', 'Ore.': 'OR', 'Pa.': 'PA', 'R.I.': 'RI', 'S.C.': 'SC',
    'S.D.': 'SD', 'Tenn.': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vt.': 'VT',
    'Va.': 'VA', 'Wash.': 'WA', 'W.Va.': 'WV', 'Wis.': 'WI', 'Wyo.': 'WY'
}


all_states = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]


def bing_api(course_name, city, state_label, bing_api_key):
    
    location = geocoder.bing(f"{course_name} {city}, {state_label}", key=bing_api_key).json

    latitude = location['lat']
    longitude = location["lng"]
    country = location["country"]

    return latitude, longitude, country
