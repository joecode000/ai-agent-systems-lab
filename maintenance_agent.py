from smolagents import CodeAgent, InferenceClientModel, tool
@tool
def diagnose_maintenance_issue(
    equipment: str,
    symptom: str,
    observations: str = "No additional observations provided",
) -> str:
    """
    Create a structured maintenance diagnostic request.

    Args:
        equipment: The machine, system, or component being examined.
        symptom: The main failure or abnormal behavior.
        observations: Alarm codes, measurements, sounds, smells, or visible evidence.
    """
    return f"""
Equipment: {equipment}
Primary symptom: {symptom}
Observed evidence: {observations}

Evaluate the following:

1. Immediate safety hazards
2. Most probable causes
3. Diagnostic checks in the safest order
4. Tools and measurements required
5. Conditions requiring escalation
"""


model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    provider="auto",
)

agent = CodeAgent(
    tools=[diagnose_maintenance_issue],
    model=model,
    max_steps=4,
)


if __name__ == "__main__":
    result = agent.run(
        """
        Diagnose the following maintenance issue.

        Equipment: commercial floor scrubber
        Symptom: machine operates, but no water reaches the floor
        Observations: solution tank contains water and the vacuum motor works

        Do not assume a component has failed without first proposing
        a verification test. Prioritize electrical and physical safety.
        """
    )

    print(result)
    