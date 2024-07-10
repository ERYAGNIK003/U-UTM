# UAV-GSD
Derivation of Ground Sample Distance (GSD) for UAV-based road traffic analytics.

Training:
We uses empirical data points given in TrainingData.csv file to find relationship between cm/px and flight height. 

Testing: 
Run rmse.py to find RMSE error in GSD mapping for rotated UAV videos. We have tested empirical GSD on 3 different videos having varying flight height and rotation. 

Dataset Description:
Videos are available on following link [GSD mapping for UAV-based video analytics]: www.youtube.com/@YagnikBhavsar.

Owners: 
Yagnik M Bhavsar, Mazad S Zaveri, and Mehul S Raval [Ahmedabad University]. 
  
Acknowledgement: 
We thank the Joint Commissioner of Traffic Police, Ahmedabad City (Gujarat,
India), for permission (under application number G/725/Traffic/3186/2021) to
fly a drone. This work was carried out as part of the seed grant number URB-
SEASI21A3, funded by the University Research Board, Ahmedabad University. The
work is also supported by the workstation with GPU purchased under the grant
GUJCOST/STI/2021–22/3858 by the Gujarat Council of Science and Technology,
Government of Gujarat, India. We thank Shaheriar B Zaveri (road safety expert) for 
guiding us throughout the journey.

Publications:
1. Bhavsar, Y.M., Zaveri, M.S., Raval, M.S., Zaveri, S.B.: Vision-based investiga-
tion of road traffic and violations at urban roundabout in india using uav video:
A case study. Transportation Engineering 14 (2023).
