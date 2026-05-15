public class ProPlan extends AIModel {

    private int availableSlots;

    public ProPlan(String modelName, double price, int parameterCount, String contextWindow, int availableSlots) {
        super(modelName, price, parameterCount, contextWindow);
        this.availableSlots = availableSlots;
    }

    public int getAvailableSlots() {
        return availableSlots;
    }

    // Add a team member — decrements one slot if available
    public String addTeamMember(String memberName) {
        if (availableSlots <= 0) {
            return "No available slots. Cannot add " + memberName + ". Please upgrade your plan.";
        }
        availableSlots--;
        return memberName + " has been added to the team. Available slots remaining: " + availableSlots;
    }

    // Remove a team member — frees up one slot
    public String removeTeamMember(String memberName) {
        availableSlots++;
        return memberName + " has been removed from the team. Available slots: " + availableSlots;
    }

    // Pro plan has unlimited prompts, just checks context window
    @Override
    public String enterPrompt(String promptText, int outputTokens) {
        int totalTokens = calculateTokens(promptText, outputTokens);
        int contextLimit = getContextWindowAsInt();

        if (totalTokens > contextLimit) {
            return "Request exceeds context window (" + getContextWindow() + "). "
                    + "Total tokens required: " + totalTokens + ". Please shorten your prompt or reduce expected output.";
        }

        return "Prompt submitted successfully. (Pro Plan - Unlimited)\n"
                + "Model   : " + getModelName() + "\n"
                + "Prompt  : " + promptText + "\n"
                + "Tokens  : " + totalTokens + " (input + output)";
    }

    @Override
    public String display() {
        return "[ Pro Plan ]\n"
                + "Model Name      : " + getModelName() + "\n"
                + "Price (per 1L tokens) : Rs. " + getPrice() + "\n"
                + "Parameters      : " + getParameterCount() + "B\n"
                + "Context Window  : " + getContextWindow() + "\n"
                + "Available Slots : " + availableSlots;
    }
}
