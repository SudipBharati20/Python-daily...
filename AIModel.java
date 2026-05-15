import java.util.ArrayList;

public abstract class AIModel {

    private String modelName;
    private double price;
    private int parameterCount;
    private String contextWindow;

    public AIModel(String modelName, double price, int parameterCount, String contextWindow) {
        this.modelName = modelName;
        this.price = price;
        this.parameterCount = parameterCount;
        this.contextWindow = contextWindow;
    }

    // Accessors
    public String getModelName() {
        return modelName;
    }

    public double getPrice() {
        return price;
    }

    public int getParameterCount() {
        return parameterCount;
    }

    public String getContextWindow() {
        return contextWindow;
    }

    // Shared token calculation logic
    // Estimates tokens from prompt text length + expected output tokens
    public int calculateTokens(String promptText, int outputTokens) {
        // rough estimate: 1 token ~ 4 characters
        int inputTokens = (int) Math.ceil(promptText.length() / 4.0);
        return inputTokens + outputTokens;
    }

    // Parse context window string like "64K" or "128K" into integer token count
    protected int getContextWindowAsInt() {
        String cw = contextWindow.trim().toUpperCase();
        try {
            if (cw.endsWith("K")) {
                return Integer.parseInt(cw.substring(0, cw.length() - 1)) * 1000;
            } else if (cw.endsWith("M")) {
                return Integer.parseInt(cw.substring(0, cw.length() - 1)) * 1_000_000;
            } else {
                return Integer.parseInt(cw);
            }
        } catch (NumberFormatException e) {
            return Integer.MAX_VALUE;
        }
    }

    public abstract String display();

    public abstract String enterPrompt(String promptText, int outputTokens);
}
