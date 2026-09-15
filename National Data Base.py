import streamlit as st
from datetime import datetime
import random

citizens= {
   citizens = {1: {"name": "Rahul",
  "family member": 5,
  "annual income": 120000,
  "adhaar number": "123456789012",
  "pan number": "ABCDE1234F",
  "phone number": "9030675972",
  "state": "West Bengal",
  "address": "14,Park Street,Mullick Bazar,Park Street area,Kolkata",
  "blood group": "A+"
  },

  2: {"name": "Aman",
  "family member": 7,
  "annual income": 600000,
  "adhaar number": "391482056173",
  "pan number": "ABCDE1234G",
  "phone number": "7644289430",
  "state": "Maharashtra",
  "address": "Plot 78,Sector 14,Vashi,Navi Mumbai",
  "blood group":"O-"
  },

  3:{"name": "Riya",
  "family member": 3,
  "annual income": 400000,
  "adhaar number": "248971325064",
  "pan number": "ABCPK5432M",
  "phone number": "6789012345",
  "state": "Rajasthan",
  "address": "Jaipur",
  "blood group": "AB-"
  },

  4:{"name": "Neha",
  "family member": 6,
  "annual income": 800000,
  "adhaar number": "450293167284",
  "pan number": "ABCPK5432M",
  "phone number": "7890123456",
  "state": "Karnataka",
  "address": "Bengaluru",
  "blood group": "AB+"
  },

  5:{"name": "Arjun",
  "family member": 10,
  "annual income": 1000000,
  "adhaar number": "513604278395",
  "pan number": "XYZPQ1234K",
  "phone number": "9567890123",
  "state": "Punjab",
  "address": "Ludhiana",
  "blood group": "A-"
  },

  6:{"name": "Priya",
  "family income":8,
  "annual income": 520000,
  "adhaar number": "678315389406",
  "pan number": "LMNHR8765P",
  "phone number": "8765432109",
  "state": "Haryana",
  "address": "Sector 15,Gurugram",
  "blood group": "O+"
  },

  7:{"name": "Karan",
  "family member": 6,
  "annual income": 300000,
  "adhaar number": "262759723840",
  "pan number": "PQRSW9876T",
  "phone number": "9876543210",
  "state":"Uttar Pradesh",
  "address": "22/A,Ashoka Marg,Civil Lines,Prayagraj",
  "blood group": "A+"
  },

  8:{"name": "Simran",
  "family member": 7,
  "annual income": 700000,
  "adhaar number": "951648612739",
  "pan number": "RTYUP4321F",
  "phone number": "7654321098",
  "state":"Tamil Nadu",
  "address": "door no.12/34,Anna Nagar 2nd Street,Velachery,Chennai",
  "blood group": "O-"
  },

  9:{"name": "Rohan",
  "family member": 3,
  "annual income": 400000,
  "adhaar number": "842537501638",
  "pan number": "GHJKL6543A",
  "phone number": "9123456780",
  "state":"Gujrat",
  "address": "shop 3,Silver Leaf Complex,Near Stadium,Navrangpura,Ahmedabad",
  "blood group": "A-"
  },

  10:{"name": "Anjali",
  "family member": 7,
  "annual income": 550000,
  "adhaar number": "733426490527",
  "pan number": "VBNMZ2468Q",
  "phone number": "8234567890",
  "state": "New Delhi",
  "address": "house no.45,Green Park Extension,New Delhi",
  "blood group": "A+"
  }
}
   
st.set_page_config(page_title="National Data Base",
layout="centered")
st.title("National Data Base (NDB")
st.caption("Government-style citizen information demo | All records are fictional dummy data.")

st.divider()

c1,c2,c3 = st.columns(3)
c1.metric("Total Citizens", len(citizens))
c2.metric("Average Annual Income",f"₹{sum(x['income]for x in citizens)//len(citizens):,}")
c3.metric("blood Groups",len(set(x["blood"] for x in citizens)))

st.divider()

st.subheader("Search Citizen")

search_type = st.selectbox(
      "Search By",
      ["Aadhaar number", "Name", "Phone Number"])
search_value = st.text_input("Enter search value")

  if search_value:
      key = {
          "Aadhar Number": "aadhaar",
          "Name": "name",
          "Phone number": "phone"}[search_type]

results = [
      person for person in citizens
      if search_value.lower() in str(person[key]).lower()]

      if results:
         for person in results:
             st.success(f"Citizen Found: {person['name']}")
             st.write(f"**Name:** {person['name']}")
             st.write(f"**Family Members:** {person['family']}")
             st.write(f"**Annual Income:** ₹{person['income']:,}")
             st.write(f"**Phone:** {person['phone']}")
             st.write(f"**Aadhaar:** {person['aadhaar']}")
             st.write(f"**PAN:** {person['pan']}")
             st.write(f"**Address:** {person['address']}")
             st.write(f"**Blood Group:** {person['blood']}")


st.divider()
         else:
             st.error("No citizen found.")


st.subheader("📋 Filter Citizen Database")

col1, col2 = st.columns(2)

with col1:
    blood_groups = ["All"] + sorted(set(x["blood"] for x in citizens))
    selected_blood = st.selectbox("Blood Group", blood_groups)

with col2:
    max_income = st.number_input(
        "Maximum Annual Income (₹)",
        min_value=0,
        value=1000000,
        step=50000
    )

filtered = citizens

if selected_blood != "All":
    filtered = [x for x in filtered if x["blood"] == selected_blood]

filtered = [x for x in filtered if x["income"] <= max_income]

st.write(f"**{len(filtered)} citizen(s) found**")

table_data = [
    {
        "Name": x["name"],
        "Family": x["family"],
        "Annual Income": f"₹{x['income']:,}",
        "Phone": x["phone"],
        "Aadhaar": x["aadhaar"],
        "PAN": x["pan"],
        "Address": x["address"],
        "Blood Group": x["blood"]
    }
    for x in filtered
]

st.dataframe(table_data, use_container_width=True, hide_index=True)


st.info(
    "Demo only: The citizen records, Aadhaar Numbers, Pan Numbers and Phone Numbers"
    "avobe are fictional and must not be treated as real government data.")
             



