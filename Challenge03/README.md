This week's challenges follow a sequential order: you need to complete challenge 1 before going on to challenge 2 and so on.
# 🟢 Challenge 1 Predictive Positive Value

The positive predictive value (PPV), the probability that a person who gets a positive test result actually has the disease or condition tested for. It helps to take into account the sensitivity and specificity of the test as well as the incidence of the disease

- Sensitivity: The probability that the test is positive given the person _has_ the disease.
- Specificity: The probability that the test is negative given the person _does not_ have the disease.
- Incidence: The baseline proportion of the population that has the disease, serves as prior knowledge

The formula to calculate the PPV is based on Bayes' rule. To compute this number it on terms of sensitivity, specificity and incidence, the next formula can be used: 

$$
\text{PPV}=\frac{\text{Incidence} \cdot \text{Sensitivity}}{\text{Incidence} \cdot \text{Sensitivity}+(1-\text{Incidence})(1-\text{Specificity})}
$$

**Main Task:** Define a function `compute_PPV()` taking `sensitivity`, `specificity` and `incidence` as arguments. 

You may use the values for the COVID-19 Rapid Antigen Test (70% sensitivity, 98% specificity) and assume it has an incidence of 5%. If you use it in the Python console with these values, the output should look as follows:

```
>> print(compute_PPV(0.7, 0.98, 0.05))
0.6481481481481479
```

# 🟠 Challenge 2 (Optional) Refining PPV Function 

Think of the following: Which is your expected input? Which cases would cause your code to break? You may make your code more resilient by adding validations. Looking back at `compute_PPV()`, which validations could improve it?

**Main Task:** Using `if`/`else` statements before running the formula in `compute_PPV()`,

- Validate that all inputs are valid probabilities between `0.0` and `1.0`, if no valid probabilities are provided, return `None` and print an appropriate error message
- Avoid division by 0, if the denominator equals 0, have `compute_PPV()` return `0.0`

Test your function in the Python console with the following values:
```
>> print(compute_PPV(70, 98, 5))
Error: All input arguments must be probabilities between 0 and 1.
None
```

```
>> print(compute_PPV(0.95, -0.7, 0.05))
Error: All input arguments must be probabilities between 0 and 1.
None
```

```
>> print(compute_PPV(0.95, 1, 0))
0.0
```

```
>> print(compute_PPV(0.95, 0.90, 0.05))
0.3333333333333334
```

# 🟡 Challenge 3 Comparing Tests

You may use PPV values to make comparisons between tests for the same disease. 

**Main Task:** Use `compute_PPV()` to compare the COVID-19 Rapid Antigen Test (70% sensitivity, 98% specificity) and the COVID-19 RT-PCR Test (95% sensitivity, 99.5% specificity) assuming a 5% disease incidence. Print the results with a brief message providing context, displaying probabilities as percentages with two decimal places. 

You may print the message as you wish, but here's an example of  what it may look like:
```
Given a COVID-19 incidence of 5.00%, the Rapid Antigen Test has a PPV of 64.81%
```

# 🟡 Challenge 4 Incidence as a Prior Belief

You may have noticed that the incidence can change; specially when we're talking about infectious diseases. There may be periods of high prevalence and low prevalence. You may use the function you created to compare how prevalence affects the PPV.

Incidence may also be affected by risk groups. So far, we assumed that we only know that the test results for the patient, but if we know other clinical variables, it may be useful to take into account more specific data. For example, if we were looking at breast cancer, different age groups have different incidences:

- Low risk group (< 40 years old): 0.4%
- Moderate risk group (40 - 49 years old): 1.5%
- High risk group (50 - 74 years old): 3.5%

Ultimately, incidence serves as a stand-in to quantify our prior belief that the patient has the disease. In Bayesian terms, the PPV is the probability that the person has the disease given that they tested positive. We are essentially updating our prior probability for the disease with the new evidence provided by the test result.

**Main Task:** Use `compute_PPV()` to analyze how prevalence affects the PPV of the COVID-19 Rapid Antigen Test (70% sensitivity, 98% specificity) by comparing positive tests results from a high-prevalence period of 20% incidence and a low-prevalence period of 1% incidence. Then, analyze the PPV for the Digital Mammography Test for Breast Cancer (97% sensitivity, 64.5% specificity) for three patients with ages 35, 45 and 55. Print the results with a brief message providing context, displaying probabilities as percentages with two decimal places. 

Example messages for this exercise:
```
Given a COVID-19 incidence of 1.00%, the Rapid Antigen Test has a PPV of xx.xx%
```

```
For a 35 year old patient, the Digital Mammography Test for Breast Cancer has a PPV of xx.xx%
```

# 🟠 Challenge 5 The Negative Predictive Value 

Similar to the PPV, the Negative Predictive Value (NPV), the probability that a person who receives a negative test result truly does not have the condition or disease. The formula for NPV is as follows:

$$
NPV = \frac{(1-\text{Incidence}) \cdot \text{Specificity}}{(1-\text{Incidence}) \cdot \text{Specificity}+\text{Incidence} \cdot (1-\text{Sensitivity})}
$$

**Main Task:** Define a function `compute_NPV()` taking `sensitivity`, `specificity` and `incidence` as arguments. Ideally, incorporate validations as you did for `compute_PPV()` in Challenge 2

You may use the values for the COVID-19 Rapid Antigen Test again (70% sensitivity, 98% specificity) and assume it has an incidence of 5%. If you use it in the Python console with these values, the output should look as follows:

```
>> print(compute_NPV(0.7, 0.98, 0.05))
0.9841437632135306
```

# 🔴 Challenge 6 Updating Beliefs

Intuitively, you may think that if you have two tests done for the same disease and they both have positive results, then the probability of having said disease is stronger. This Bayesian framework allows us to quantify this if we replace incidence with the PPV of the first test, which would represent the current probability of having the disease.

**Main Task:** Compute the probability of having COVID-19 given that a patient tested positive on the COVID-19 Rapid Antigen Test (70% sensitivity, 98% specificity) and then tested positive on the COVID-19 RT-PCR Test (95% sensitivity, 99.5% specificity), assuming the prevalence was 1%. Then, incorporate the NPR function to compute the probability of having COVID-19 given that a patient tested positive on the COVID-19 Rapid Antigen Test and then tested negative on the COVID-19 RT-PCR Test. *Hint: The probability of having the disease given a negative result is 1 - NPV.* Print the results in a message providing context:

```
Probability after 1st Positive (Antigen): 26.12%
Probability after 1st Positive THEN 2nd Positive (PCR): 98.49%
Probability after 1st Positive THEN 2nd Negative (PCR): 1.74%
```

Finally, reflect on how the use of functions can improve your workflow when dealing with analysis in which you have to do the same task (such as computing the PPV) multiple times. 