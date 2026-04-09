#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

struct BankNode {
    std::string symbol;
    double marketCap;
    double beta;
};

int main() {
    std::vector<BankNode> cluster = {
        {"JPM",  851.34, 1.10},
        {"BAC",  383.95, 1.25},
        {"HSBC", 290.10, 0.95},
        {"MS",   272.57, 1.40},
        {"WFC",  252.56, 1.15}
    };
    const double shock_magnitude = -0.015; 
    std::cout << "--- STARGATE VOLATILITY STRESS-TEST (April 8, 2026) ---" << std::endl;
    for (const auto& bank : cluster) {
        double loss = bank.marketCap * (shock_magnitude * bank.beta);
        double post_shock = bank.marketCap + loss;
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "BANK: " << bank.symbol 
                  << " | LOSS: $" << std::abs(loss) << "BN"
                  << " | RESIDUAL: $" << post_shock << "BN" << std::endl;
    }
    return 0;
}
