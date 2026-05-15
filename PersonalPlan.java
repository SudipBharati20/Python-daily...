public class PersonalPlan extends AIModel {

    private int promptsRemaining;

    public PersonalPlan(String modelName, double price, int parameterCount, String contextWindow, int promptsRemaining) {
        super(modelName, price, parameterCount, contextWindow);
        this.promptsRemaining = promptsRemaining;
    }

    public int getPromptsRemaining() {
        return promptsRemaining;
    }

    // Buy (add) additional prompts to the monthly quota
    public String buyPrompts(int amount) {
        if (amount <= 0) {
            return "Please enter a positive number of prompts, or consider upgrading to Pro Plan.";
        }
        promptsRemaining += amount;
        return amount + " prompt(s) added. Prompts remaining: " + promptsRemaining;
    }

    @Override
    public String enterPrompt(String promptText, int outputTokens) {
        if (promptsRemaining <= 0) {
            return "Monthly prompt limit reached. Please buy more prompts or upgrade to Pro Plan.";
        }

        int totalTokens = calculateTokens(promptText, outputTokens);
        int contextLimit = getContextWindowAsInt();

        if (totalTokens > contextLimit) {
            return "Request exceeds context window (" + getContextWindow() + "). "
                    + "Total tokens required: " + totalTokens + ". Please shorten your prompt or reduce the expected output length.";
        }

        promptsRemaining--;
        return "Prompt submitted successfully.\n"
                + "Model     : " + getModelName() + "\n"
                + "Prompt    : " + promptText + "\n"
                + "Tokens    : " + totalTokens + " (input + output)\n"
                + "Prompts remaining: " + promptsRemaining;
    }

    @Override
    public String display() {
        return "[ Personal Plan ]\n"
                + "Model Name      : " + getModelName() + "\n"
                + "Price (per 1L tokens) : Rs. " + getPrice() + "\n"
                + "Parameters      : " + getParameterCount() + "B\n"
                + "Context Window  : " + getContextWindow() + "\n"
                + "Prompts Remaining: " + promptsRemaining;
    }
}
