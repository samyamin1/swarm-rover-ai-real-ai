#!/usr/bin/env python3
"""
Performance Analyzer for Swarm Rover AI Simulation
Analyzes and reports on simulation performance metrics
"""

import json
import os
import matplotlib.pyplot as plt

class PerformanceAnalyzer:
    def __init__(self, report_dir="./testing/reports/"):
        self.report_dir = report_dir
        os.makedirs(self.report_dir, exist_ok=True)
        self.metrics_history = []

    def record_metrics(self, metrics: dict):
        """Records a snapshot of current simulation metrics."""
        self.metrics_history.append(metrics)

    def generate_report(self, scenario_name: str = "default_scenario"):
        """Generates a comprehensive performance report."""
        if not self.metrics_history:
            print("No metrics recorded to generate report.")
            return

        report_filename = f"performance_report_{scenario_name}_{int(os.times().elapsed)}.json"
        report_filepath = os.path.join(self.report_dir, report_filename)

        with open(report_filepath, 'w') as f:
            json.dump(self.metrics_history, f, indent=4)
        print(f"Performance report saved to {report_filepath}")

        self._plot_metrics(scenario_name)

    def _plot_metrics(self, scenario_name: str):
        """Plots key performance metrics over time."""
        if not self.metrics_history:
            return

        timestamps = [i for i in range(len(self.metrics_history))]
        mission_success_rates = [m["mission_success_rate"] for m in self.metrics_history]
        formation_accuracies = [m["formation_accuracy"] for m in self.metrics_history]
        communication_efficiencies = [m["communication_efficiency"] for m in self.metrics_history]

        plt.figure(figsize=(12, 8))

        plt.subplot(3, 1, 1)
        plt.plot(timestamps, mission_success_rates, label="Mission Success Rate")
        plt.title(f"Performance Metrics for {scenario_name}")
        plt.ylabel("Success Rate (%)")
        plt.grid(True)
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(timestamps, formation_accuracies, label="Formation Accuracy")
        plt.ylabel("Accuracy (%)")
        plt.grid(True)
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(timestamps, communication_efficiencies, label="Communication Efficiency")
        plt.xlabel("Time Steps")
        plt.ylabel("Efficiency (%)")
        plt.grid(True)
        plt.legend()

        plt.tight_layout()
        plot_filename = f"performance_plot_{scenario_name}_{int(os.times().elapsed)}.png"
        plot_filepath = os.path.join(self.report_dir, plot_filename)
        plt.savefig(plot_filepath)
        print(f"Performance plot saved to {plot_filepath}")
        plt.close()

if __name__ == "__main__":
    # Example Usage:
    analyzer = PerformanceAnalyzer()

    # Simulate some metric recording
    for i in range(100):
        metrics = {
            "mission_success_rate": random.uniform(50, 100),
            "formation_accuracy": random.uniform(70, 95),
            "communication_efficiency": random.uniform(80, 100),
            "average_response_time": random.uniform(0.1, 1.5),
            "targets_found": i // 10,
            "total_targets": 10
        }
        analyzer.record_metrics(metrics)

    analyzer.generate_report("example_scenario")
