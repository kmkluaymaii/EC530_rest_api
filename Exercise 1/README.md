## User Story for FDA API
"As a user I want to be able to look up the historical adverse events of a number of patients after taking a specific drugs."

## Example usage
If the user wants to know the adverse events of Paracetamol from 10 patients, the user can run `get_adverse_events("PARACETAMOL", 10)`
And it will print out the result like 
```
Adverse Effect for Paracetamol !!

Patient 1 Adverse Effect
 - Reaction: Erection increased

Patient 2 Adverse Effect
 - Reaction: Fall
 - Reaction: Rhabdomyolysis
 - Reaction: Somnolence

Patient 3 Adverse Effect
 - Reaction: Rectocele

Patient 4 Adverse Effect
 - Reaction: Cerebral venous thrombosis
 - Reaction: Jugular vein thrombosis

Patient 5 Adverse Effect
 - Reaction: Bone marrow failure
 - Reaction: Pyrexia
 - Reaction: Neutropenia
 - Reaction: Leukopenia
 - Reaction: Thrombocytopenia
 - Reaction: Pancytopenia
 - Reaction: Tonsillitis
 - Reaction: Cough
 - Reaction: Tonsillar hypertrophy
 - Reaction: Purulent discharge
 - Reaction: Pharyngeal erythema
 - Reaction: Odynophagia
 - Reaction: Lymphadenopathy
 - Reaction: Productive cough

Patient 6 Adverse Effect
 - Reaction: Grand mal convulsion
 - Reaction: Postictal state

Patient 7 Adverse Effect
 - Reaction: Hypoaesthesia oral
 - Reaction: Hypoaesthesia

Patient 8 Adverse Effect
 - Reaction: Vomiting
 - Reaction: Diplopia
 - Reaction: Gait disturbance
 - Reaction: Balance disorder
 - Reaction: Dyspnoea
 - Reaction: Gastroenteritis
 - Reaction: Dizziness

Patient 9 Adverse Effect
 - Reaction: Femur fracture
 - Reaction: Incorrect drug administration duration

Patient 10 Adverse Effect
 - Reaction: Death
```
